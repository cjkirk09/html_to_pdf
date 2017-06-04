"""
PDF utility functions
"""
# Deprecation warnings generated by python2.6 using pyPdf
import warnings

warnings.filterwarnings('ignore')

import commands
import re
import tempfile

from flask import render_template, send_file
# wkhtmltopdf binary location
wkhtml_bin = 'bin/wkhtmltopdf'


def sub_rel_refs(html, tags, baseurl):
    """
    Replace all instances of relative links in `html` with an absolute link
    based on `baseurl` for the given `tags`

    `tags`  a list of zero or more of the following
            a, script, link, img, input
    """
    regex_rel = r'(<\s*%s.*?%s="?)(?!http)(?!/)(?!#)((?!").*?)("?[\s>])'
    regex_root = r'(<\s*%s.*?%s="?)(?!http)(?!#)((?!")/.*?)("?[\s>])'
    tagattribs = {
        'a': 'href',
        'script': 'src',
        'link': 'href',
        'img': 'src',
        'input': 'src',
    }
    repls = []
    for tag in tags:
        attrib = tagattribs.get(tag.lower())

        r = re.compile(regex_rel % (tag.lower(), attrib), re.I | re.U)
        repl = r'\1%s/\2\3' % baseurl
        html = r.sub(repl, html)

        r = re.compile(regex_root % (tag.lower(), attrib), re.I | re.U)
        repl = r'\1%s\2\3' % baseurl
        html = r.sub(repl, html)
    return html


def sub_refs(html, static_url=None, link_url=None):
    """
    `html`          HTML text
    `static_url`    base url for static content
    `link_url`      base url for relative links
    """
    if static_url:
        html = sub_rel_refs(html, ['img', 'script', 'link', 'input'], static_url)
    if link_url:
        html = sub_rel_refs(html, ['a'], link_url)
    return html


def html_to_pdf(body, url=None, coverpage=None, header=None, footer=None, static_url=None, link_url=None,
                paper_size=None, orientation=None, margins=None, print_media=True,
                no_smart_shrinking=False):
    """
    Generates a pdf file from HTML.  Returns a handle to a NamedTemporaryFile
    containing the PDF data.

    `body`      HTML text for the body
    `coverpage` HTML text for the coverpage -- no header or footer
    `header`    HTML text for the header -- see header_footer_jscript
    `footer`    HTML text for the footer -- see header_footer_jscript
    `static_url`    base url for static content
    `link_url`      base url for links

    `paper_size`    "letter" (default) or "a4"
    `orientation`   "portrait" (default) or "landscape"
    `margins`       tuple (top, right, bottom, left) - each defaults to 10mm
    `print_media`   use css @media(print) rules, True by default

    """
    global wkhtml_bin

    args = [wkhtml_bin]

    if header:
        header_file = tempfile.NamedTemporaryFile('w', prefix='htmlheader', suffix='.html')
        header_file.write(sub_refs(header, static_url, link_url))
        header_file.flush()
        args.extend(['--header-html', header_file.name, '--header-spacing', '0'])

    if footer:
        footer_file = tempfile.NamedTemporaryFile('w', prefix='htmlfooter', suffix='.html')
        footer_file.write(sub_refs(footer, static_url, link_url))
        footer_file.flush()
        args.extend(['--footer-html', footer_file.name, '--footer-spacing', '0'])

    if paper_size in ['letter', 'a4']:
        args.extend(['--page-size', paper_size])

    if orientation in ['portrait', 'landscape']:
        args.extend(['--orientation', orientation])

    if margins:
        top, right, bottom, left = margins
        args.extend(['-T', top, '-R', right, '-B', bottom, '-L', left])

    if coverpage:
        coverpage_file = tempfile.NamedTemporaryFile('w', prefix='htmlcover', suffix='.html')
        coverpage_file.write(sub_refs(coverpage, static_url, link_url))
        coverpage_file.flush()
        args.extend(['cover', coverpage_file.name])

    if print_media:
        args.append('--print-media-type')

    if no_smart_shrinking:
        args.append('--disable-smart-shrinking')

    if body:
        body = body.encode('utf-8', 'ignore')  # remove unicode characters
        body_file = tempfile.NamedTemporaryFile('w', prefix='htmlbody', suffix='.html')
        body_file.write(sub_refs(body, static_url, link_url))
        body_file.flush()
        args.append(body_file.name)
    else:
        args.append(url)

    ofile = tempfile.NamedTemporaryFile('w+b', prefix='pdfoutput', suffix='.pdf')
    args.append(ofile.name)

    # all command line args have been generated in this file and are safe except
    # for wkhtml_bin... which we'll assume is safe.
    cmd = ' '.join(args)
    print cmd
    status, output = commands.getstatusoutput(cmd)
    if status:
        raise Exception('Error generating PDF: %s' % output)
    return ofile


def generatePdf(path, no_smart_shrinking=False):
    # html = render_template(path)
    footer = render_template('default_footer.html')
    header = render_template('default_header.html')
    stream = html_to_pdf(None, url='http://localhost:5000/' + path, footer=footer, header=header,
                         margins=('1in', '0.5in', '1in', '0.5in'), static_url="http://localhost:5000",
                         paper_size="letter", no_smart_shrinking=no_smart_shrinking)

    # read to the end to get the size
    stream.seek(0, 2)
    filesize = stream.tell()
    # get back to the start of the file to read it out
    stream.seek(0)
    return send_file(stream, 'application/pdf', True, '{0}.pdf'.format(path or 'index'))
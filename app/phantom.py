import subprocess
from tempfile import NamedTemporaryFile
from flask import send_file


def html_to_pdf(homepath, path, landscape='f'):
    """
    I make a request to C{url} and return the contents as a PDF.

    @ivar read: If True, I return the contents of the PDF file.  If False,
        I return the file object.
    """

    pdf_file = NamedTemporaryFile(suffix='.pdf')
    phantomjs_bin = 'bin/phantomjs'
    flags = '--ignore-ssl-errors=true --ssl-protocol=any'
    rasta_js = '/static/js/rasta.js'
    orientation = 'landscape' if landscape == 't' else 'portrait'
    cmd = '%s %s %s %s "%s" %s' % (
        phantomjs_bin, flags, rasta_js, homepath + path, pdf_file.name, orientation)
    retcode = subprocess.call(cmd, shell=True)
    if retcode:
        print("PDF generation failed with returncode %d" % retcode)
        return

    return pdf_file



def generatePdf(path):
    stream = html_to_pdf('http://localhost:5000/', path)
    # read to the end to get the size
    stream.seek(0, 2)
    filesize = stream.tell()
    # get back to the start of the file to read it out
    stream.seek(0)
    return send_file(stream, 'application/pdf', True, '{0}.pdf'.format(path or 'index'))
import json
import re
import subprocess
import urllib

from tempfile import NamedTemporaryFile




def html_to_pdf(path, read=True, password=None, customer=None, landscape='f'):
    """
    I make a request to C{url} and return the contents as a PDF.

    @ivar read: If True, I return the contents of the PDF file.  If False,
        I return the file object.
    """

    pdf_file = NamedTemporaryFile(suffix='.pdf')
    phantomjs_bin = '/bin/phantomjs'
    flags = '--ignore-ssl-errors=true --ssl-protocol=any'
    rasta_js = '/static/js/rasta_js'
    orientation = 'landscape' if landscape == 't' else 'portrait'
    cmd = '%s %s %s %s "%s" %s' % (
        phantomjs_bin, flags, rasta_js, path, pdf_file.name, orientation)
    retcode = subprocess.call(cmd, shell=True)
    if retcode:
        print("PDF generation failed with returncode %d" % retcode)
        return

    return pdf_file



def generatePdf(path):
    pass
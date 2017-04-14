/*
This is a Phantom JS control script that accepts four commandline arguments.
And converts the passed URL into a PDF.

Usage:
phantomjs rasta.js [URL] [output.file] [orientation]
*/


// REQUIREMENTS
var page = require('webpage').create(),
    system = require('system'),
    fs = require('fs'),
    address, output, orientation;


// Parse the arguments
address = system.args[1];
output = system.args[2];
orientation = system.args[3];


// Setup renderer options
page.paperSize = {
  format: 'A4',
  orientation: orientation,
  border: '1cm'
};


page.onResourceError = function(resourceError) {
    page.reason = resourceError.errorString;
    page.reason_url = resourceError.url;
};


// open the page and rasta time
page.open(address, function (status) {
    if (status !== 'success') {
        console.log(page.reason);
        phantom.exit(1);
    } else {
        page.render(output, { format: 'pdf' });
        phantom.exit(0);
    }
});
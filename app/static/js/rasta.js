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
    format: 'Letter',
    orientation: orientation,
    margin: {
        top: '1cm',
        left: '1cm',
        right: '1cm',
        bottom: '1cm'
    },
    header: {
        height: "1cm",
        contents: phantom.callback(function(pageNum, numPages) {
            return "<div>Header <span style='float:right'>" + pageNum + " / " + numPages + "</span></div>";
        })
    },
    footer: {
        height: "1cm",
        contents: phantom.callback(function(pageNum, numPages) {
        return "<h1>Footer <span style='float:right'>" + pageNum + " / " + numPages + "</span></h1>";
        })
    }
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
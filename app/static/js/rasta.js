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
            return "<div><span style='float:right; font-size: 10px;'>Page " + pageNum + " of " + numPages + "</span></div>";
        })
    },
    footer: {
        height: "1cm",
        contents: phantom.callback(function(pageNum, numPages) {
        return "<div style='font-size: 10px;'><span style='color: gray;'>" + pageNum + " &copy; Made using PhantomJS</span><span style='float:right'>Sadly, No Image</span></div>";
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
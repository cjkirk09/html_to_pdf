TODO Make this accurate

pip install flask

wkhtmltopdf (0.12.4 with patched qt) requires zlib, fontconfig, freetype, and X11 libs(libX11, libXext, libXrender)

phantomjs (2.1.1) requires fontconfig or libfontconfig the system must have GLIBCXX_3.4.9 and GLIBC_2.7.


# to run the server
python server.py [-d]

-d is an optional flag to set the Flask server in debug mode which will reload your server when you make changes

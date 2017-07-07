TODO Make this accurate

pip install flask

wkhtmltopdf (0.12.4 with patched qt) requires zlib, fontconfig, freetype, and X11 libs(libX11, libXext, libXrender)

phantomjs (2.1.1) requires fontconfig or libfontconfig the system must have GLIBCXX_3.4.9 and GLIBC_2.7.


# to run the Docker container of this server
This whole server has been Dockerized because it needs to run Linux since it uses the Linux binaries of wkhtmltopdf and phantomjs. So to use the Docker container:
Get into the root directory of this project and run
`docker-compose up`

This build the container if you don't already have it. This could take a while. If the container already is built, then it will spin the server up in debug mode on port 5000.


# to run the server directly
python server.py [-d]

-d is an optional flag to set the Flask server in debug mode which will reload your server when you make changes

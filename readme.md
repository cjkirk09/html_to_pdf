This is a Dockerized server for testing the capabilities of PhantomJS and wkhtmltopdf. It is running a simple Flask server on Ubuntu with Linux binaries for both technologies.

Uses:

wkhtmltopdf (version 0.12.4 with patched qt) https://wkhtmltopdf.org/index.html

phantomjs (version 2.1.1) http://phantomjs.org/

Flask (version 0.12.1) http://flask.pocoo.org/docs/0.12/

python (version 2.7)


# to generate pdfs on this server
If you want to generate a pdf using PhantomJS:

- on any endpoint place `/ph` in front of the path to the page you want.

example:

- If you want to make a pdf of the page at http://localhost:5000/hello, then you would make the query http://localhost:5000/ph/hello in the browser



If you want to generate a pdf using wkhtmltopdf:

- on any endpoint place `/wk` in front of the path to the page you want.

example:

- If you want to make a pdf of the page at http://localhost:5000/hello, then you would make the query http://localhost:5000/wk/hello in the browser


wkhtmltopdf has a few extra features:

- to include the default coverpage: http://localhost:5000/wk/hello?cp=t
- to turn off smart shrinking: http://localhost:5000/wk/hello?nss=t


# to run the docker container of this server
This whole server has been Dockerized because it needs to run Linux since it uses the Linux binaries of wkhtmltopdf and phantomjs. So to use the Docker container:

Get into the root directory of this project and run

`docker-compose up`

This will build the container if you don't already have it. This could take a while. If the container already is built, then it will spin the server up in debug mode on port 5000.


# to run the server directly
To do this, you must be on a linux machine.

You will first need to install the proper libraries

`apt-get update -y && apt-get install -y python-pip python-dev build-essential libx11-dev fontconfig libxrender-dev libxext-dev wget`

`pip install -r requirements.txt`

Then you can run the server like this:

`python server.py [-d]`

-d is an optional flag to set the Flask server in debug mode which will reload your server when you make changes

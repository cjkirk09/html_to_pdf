FROM ubuntu:16.04
MAINTAINER Cory Kirkland "cory@securitymetrics.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y libx11-dev fontconfig libxrender-dev libxext-dev
#RUN apt-get install freetype
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python server.py -d
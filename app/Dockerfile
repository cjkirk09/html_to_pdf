FROM ubuntu:16.04
MAINTAINER Cory Kirkland "cory@securitymetrics.com"
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential libx11-dev fontconfig libxrender-dev libxext-dev wget
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python server.py -d
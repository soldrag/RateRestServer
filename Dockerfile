FROM python:3.7.7-buster
MAINTAINER Artem Smirnov 'soldrag@gmail.com'
RUN apt-get update -y
COPY . /app
WORKDIR /app
ENTRYPOINT ['python']
CMD ['app.py']
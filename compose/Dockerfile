FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/opt
COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install --yes libgdal-dev netcat \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && adduser --disabled-password webserver

WORKDIR /usr/src/bin
COPY ./compose/bin .
RUN chmod +x /usr/src/bin/entrypoint.sh

WORKDIR /usr/src/app
COPY app .

RUN chown -R webserver .
USER webserver:webserver

FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

ARG BUILD_DEPS="build-dependencies build-base gcc libffi-dev libgcc zlib-dev linux-headers python3-dev"
ARG RUNTIME_DEPS="libxml2-dev postgresql-dev libxslt-dev jpeg-dev"

WORKDIR /usr/src/opt
COPY requirements.txt .

RUN apk update \
    && apk add --no-cache --virtual ${BUILD_DEPS} \
    && apk add --no-cache ${RUNTIME_DEPS} \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del ${BUILD_DEPS} \
    && apk add bash \
    && adduser -D webserver

WORKDIR /usr/src/bin
COPY ./compose/bin .
RUN chmod +x /usr/src/bin/entrypoint.sh

WORKDIR /usr/src/app
COPY app .

RUN chown -R webserver .
USER webserver:webserver

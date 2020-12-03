FROM python:3.7-slim

ENV CONTAINER_HOME=/usr/src

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN pip install -r $CONTAINER_HOME/requirements.txt
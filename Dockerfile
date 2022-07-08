# syntax=docker/dockerfile:1

FROM python:slim-buster

WORKDIR /app
COPY ./mysite/ ./mysite/
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /app/mysite

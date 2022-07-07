# syntax=docker/dockerfile:1

FROM python:3.9.4-alpine

WORKDIR /app
COPY ./mysite/ ./mysite/
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
# WORKDIR /app/mysite

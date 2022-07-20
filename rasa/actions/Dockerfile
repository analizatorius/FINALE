# syntax=docker/dockerfile:1

FROM rasa/rasa_core_sdk:latest
WORKDIR /app
COPY requirements.txt requirements.txt
USER root
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
EXPOSE 5055
USER 1001
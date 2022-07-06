# syntax=docker/dockerfile:1

FROM python:3.9.4-alpine

WORKDIR /app
COPY ./mysite .
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

WORKDIR /app/mysite
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
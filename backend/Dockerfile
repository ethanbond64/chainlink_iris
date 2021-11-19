# Server 

FROM python:3.7.5-slim-buster

RUN apt-get update && apt-get install -qq -y \
    build-essential libpq-dev --no-install-recommends

ENV SERVER_PATH /server
RUN mkdir -p $SERVER_PATH

WORKDIR $SERVER_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -w 4 -b 0.0.0.0:8000 "server.app:create_app()"

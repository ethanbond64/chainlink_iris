# Server 

FROM python:3.7.5-slim-buster

RUN apt-get update 
RUN apt-get install -qq -y \
    build-essential libpq-dev --no-install-recommends
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install tesseract-ocr -y


ENV SERVER_PATH /server
RUN mkdir -p $SERVER_PATH

WORKDIR $SERVER_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -w 4 -b 0.0.0.0:8000 "server.app:create_app()"

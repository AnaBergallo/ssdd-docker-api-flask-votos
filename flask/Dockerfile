FROM python:3.8-alpine

COPY main.py /home/

COPY app.ini /home/

RUN apk add python3-dev build-base linux-headers pcre-dev uwsgi postgresql-dev libpq

RUN pip3 install uwsgi flask flask_restful Flask-SQLAlchemy psycopg2-binary requests

RUN pip install flask-migrate

WORKDIR  /home

CMD ["uwsgi", "/home/app.ini"]

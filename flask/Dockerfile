FROM python:3.8-alpine

COPY app /home/app

COPY main.py /home/

COPY app.ini /home/

RUN apk add python3-dev build-base linux-headers pcre-dev uwsgi build-base postgresql-dev libpq

RUN pip install uwsgi flask flask_restful Flask-SQLAlchemy psycopg2-binary


WORKDIR  /home

CMD ["uwsgi", "/home/app.ini"]

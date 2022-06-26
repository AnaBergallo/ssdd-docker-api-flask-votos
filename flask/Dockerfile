FROM python:3.8-alpine

RUN apk add python3-dev build-base linux-headers pcre-dev uwsgi postgresql-dev libpq
#RUN pip3 install uwsgi flask flask_restful Flask-SQLAlchemy psycopg2-binary requests flask-
#RUN pip install flask-migrate

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY main.py /home/
COPY app /home/app/
COPY app.ini /home/

#WORKDIR  /home

EXPOSE 8080

CMD ["uwsgi", "/home/app.ini"]
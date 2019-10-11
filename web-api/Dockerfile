FROM python:3.7.4

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /var/www/src/
COPY ./python/src/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "--ini", "/var/www/src/uwsgi.ini"]

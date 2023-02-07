FROM python:3.10.9-alpine

WORKDIR /usr/src/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
    # EXPOSE 8000
    # RUN python manage.py runserver 0.0.0.0:8000
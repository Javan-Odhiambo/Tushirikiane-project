# Pull base image
FROM python:alpine3.17

# Set work directory
WORKDIR /code

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=caselog.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3

# Install system and required packages required by Wagtail and Django.
RUN apk update && \
    apk add curl wget

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Run application
CMD gunicorn caselog.wsgi:application --bind 0.0.0.0:$PORT --log-file -
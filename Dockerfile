FROM python:3.8.13

WORKDIR /app

COPY setup.py /app
COPY requirements.txt /app
COPY dev-requirements.txt /app

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r dev-requirements.txt

COPY /tech_news /app/tech_news

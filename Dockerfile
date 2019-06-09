FROM python:alpine

EXPOSE 5000

RUN adduser -D vedetra

WORKDIR /home/vedetra

COPY requirements.txt requirements.txt

RUN apk --update add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
 && apk --update add --no-cache postgresql-client \
 && python -m venv venv \
 && venv/bin/pip install --no-cache-dir -r requirements.txt \
 && apk del --no-cache .build-deps

USER vedetra

COPY app app
COPY tests tests
COPY migrations migrations
COPY vedetra-server.py config.py  entrypoint.sh ./

ENTRYPOINT ["./entrypoint.sh"]


FROM python:alpine

EXPOSE 5000

ENV FLASK_APP tfg-server.py
ENV FLASK_CONFIG development

RUN adduser -D vedetra

WORKDIR /home/vedetra

COPY requirements.txt requirements.txt

RUN apk --update add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
 && python -m venv venv \
 && venv/bin/pip install --no-cache-dir -r requirements.txt \
 && apk del --no-cache .build-deps 

USER vedetra

COPY app app
COPY migrations migrations
COPY tfg-server.py config.py  entrypoint.sh ./

ENTRYPOINT ["./entrypoint.sh"]


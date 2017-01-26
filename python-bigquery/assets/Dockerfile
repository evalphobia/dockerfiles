FROM python:3.5-alpine

RUN apk add --update curl make gcc g++ \
    && rm -rf /var/cache/apk/*

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install --upgrade pip

RUN pip install boto BigQuery-GCS BigQuery-Python oauth2client

ENTRYPOINT ["python", "/opt/project/main.py"]

FROM python:3.5-alpine

RUN apk add --update curl gcc g++ \
    && rm -rf /var/cache/apk/*

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install bottle numpy cython pandas


COPY ./server.py /opt/
COPY ./prime.py /opt/
RUN sed -e "s@re.findall(ur@re.findall(r@g" /opt/prime.py > /opt/prime3.py

EXPOSE 8080 8080

ENTRYPOINT ["python", "/opt/server.py"]

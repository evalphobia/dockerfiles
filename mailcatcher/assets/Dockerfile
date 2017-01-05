FROM ruby:2.3-alpine

RUN apk add --update make gcc g++ sqlite-dev \
    && rm -rf /var/cache/apk/* \
    && gem install mailcatcher -v 0.6.4

EXPOSE 1025 1080

ENTRYPOINT ["mailcatcher", "-f", "--ip=0.0.0.0"]

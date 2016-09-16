FROM ruby:2.3-alpine

RUN apk add --update curl \
    && rm -rf /var/cache/apk/* \
    && gem install fake_sqs \
    && curl -L https://github.com/evalphobia/go-sqs-create/releases/download/v1.0.0/go-sqs-create_linux_amd64 -o /usr/local/bin/go-sqs-create \
    && chmod +x /usr/local/bin/go-sqs-create

EXPOSE 4568

CMD fake_sqs -d --pid /var/run/fake_sqs.pid --log /var/log/fake_sqs.log \
    && /usr/local/bin/go-sqs-create $SQS_QUEUES \
    ; tail -f /var/log/fake_sqs.log

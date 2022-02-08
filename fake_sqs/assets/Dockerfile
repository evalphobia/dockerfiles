FROM ruby:2.2 as builder

RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='amd64';; \
    arm64) ARCH='arm64';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -L https://github.com/evalphobia/go-sqs-create/releases/download/v1.0.3/go-sqs-create_linux_${ARCH}.gz -o go-sqs-create.gz \
    && gunzip go-sqs-create.gz \
    && chmod +x go-sqs-create \
    && mv go-sqs-create /usr/local/bin/go-sqs-create

FROM asyncaws/testing-sqs

COPY --from=builder /usr/local/bin/go-sqs-create /usr/local/bin/go-sqs-create

EXPOSE 4568

CMD /usr/local/bundle/bin/fake_sqs \
      --database=/messages/sqs/database.yml \
      --bind 0.0.0.0 \
      --port 4568 \
      --server thin \
      --pid /home/docker/fake_sqs.pid \
      --log /home/docker/fake_sqs.log \
      -d \
    && /usr/local/bin/go-sqs-create $SQS_QUEUES \
    ; tailf /home/docker/fake_sqs.log

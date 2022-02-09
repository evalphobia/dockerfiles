FROM ruby:2.7 as builder

RUN gem install mailcatcher -v 0.8.1 \
    && rm -rf /usr/local/bundle/cache/*

FROM ruby:2.7-slim

RUN apt-get update \
  && apt-get install -y sqlite3 libsqlite3-dev \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bundle /usr/local/bundle/

EXPOSE 1025 1080

ENTRYPOINT ["mailcatcher", "-f", "--ip=0.0.0.0"]

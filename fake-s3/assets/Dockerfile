FROM ruby:2.7 as builder

RUN gem install fakes3 -v 1.2.1 \
    && rm -rf /usr/local/bundle/cache/*

FROM ruby:2.7-slim

COPY --from=builder /usr/local/bundle /usr/local/bundle/

VOLUME /s3_data
RUN mkdir -p /s3_data \
    && chown nobody:nogroup /s3_data \
    && chmod 750 /s3_data

EXPOSE 4567

USER nobody
ENTRYPOINT ["/usr/local/bundle/bin/fakes3", "--port", "4567"]
CMD ["--root", "/s3_data"]

FROM ruby:2.3-alpine

EXPOSE 4567

RUN gem install fakes3

VOLUME /s3_data
RUN mkdir -p /s3_data \
    && if [ ! -z "$S3_BUCKETS" ]; then for b in "$S3_BUCKETS"; do mkdir /s3_data/$b; done fi \
    && chown -R nobody:nobody /s3_data \
    && chmod -R 750 /s3_data

USER nobody
ENTRYPOINT ["/usr/local/bundle/bin/fakes3", "--port", "4567"]
CMD ["--root", "/s3_data"]

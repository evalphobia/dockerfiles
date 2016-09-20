FROM ruby:2.3-alpine

RUN gem install fake_sns

EXPOSE 9293

ENV RACK_ENV=production
CMD ["fake_sns"]

FROM node:17.4 as node

RUN npm install -g dynamodb-admin

FROM alpine/curl:3.14 as curl

RUN cd /usr/lib && \
    curl -L https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz | tar xz

FROM openjdk:8-jre-slim

COPY nginx-proxy.conf /etc/nginx-proxy.conf
COPY supervisord.conf /etc/supervisord.conf

RUN mkdir -p /var/lib/dynamodb
VOLUME /var/lib/dynamodb

RUN apt-get update && \
    apt-get install -y supervisor nginx && \
    apt-get clean && \
    rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY --from=node /usr/local/bin /usr/local/bin/
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules/
COPY --from=node /opt /opt/
COPY --from=curl /usr/lib/DynamoDBLocal.jar /usr/lib/DynamoDBLocal.jar
COPY --from=curl /usr/lib/DynamoDBLocal_lib /usr/lib/DynamoDBLocal_lib

COPY nginx-proxy.conf /etc/nginx-proxy.conf
COPY supervisord.conf /etc/supervisord.conf
RUN ln -s /usr/local/openjdk-8/bin/java /usr/bin/java
RUN mkdir -p /var/log/supervisord

# Configuration for dynamo-admin to know where to hit dynamo.
ENV DYNAMO_ENDPOINT http://localhost:8002/

# For dinghy users.
ENV VIRTUAL_HOST dynamo.docker
ENV VIRTUAL_PORT 8000

# Main proxy on 8000, dynamo-admin on 8001, dynamodb on 8002
EXPOSE 8000 8001 8002

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

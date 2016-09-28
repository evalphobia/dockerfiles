FROM elasticsearch

RUN bin/plugin install mobz/elasticsearch-head \
    && bin/plugin install royrusso/elasticsearch-HQ \
    && bin/plugin install polyfractal/elasticsearch-inquisitor \
    && bin/plugin install analysis-kuromoji

ADD ./elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml

EXPOSE 9200

CMD  ["bin/elasticsearch", "-Des.insecure.allow.root=true"]

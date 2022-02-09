fake_sqs
====

docker-compose file for [iain/fake_sqs](https://github.com/iain/fake_sqs) which is local fake AWS SQS server.

# Usage

- 1. replace `environment` on `docker-compose.yml`
    - SQS_QUEUES: queue names to create (whitespace separated list)
- 2. up docker

example:

```bash
# 1.
    $ vi docker-compose.yml

# 2.
    $ docker-compose up
```

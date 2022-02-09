dockerfiles
----

This repository contains the Dockerfiles for my personal use.

These images supports linux/amd64 and linux/arm64.

- [dynamo-local-admin](https://hub.docker.com/r/evalphobia/dynamo-local-admin/tags)
    - Dockerfile for [instructure/dynamo-local-admin-docker](https://github.com/instructure/dynamo-local-admin-docker) which is local fake AWS DynamoDB server.
- [fake_sqs](https://hub.docker.com/r/evalphobia/fake_sqs/tags)
    - Dockerfile for [async-aws/testing-sqs](https://github.com/async-aws/testing-sqs) (fork of [iain/fake_sqs](https://github.com/iain/fake_sqs) which is local fake AWS SQS server.
- [mailcatcher](https://hub.docker.com/r/evalphobia/mailcatcher/tags)
    - Dockerfile for [mailcatcher](https://mailcatcher.me/) which is mail debugger with web interface.

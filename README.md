# Kafka Crypto matching Order engine Integration


[![Kafka](https://img.shields.io/badge/streaming_platform-kafka-black.svg?style=flat-square)](https://kafka.apache.org)
[![Docker Images](https://img.shields.io/badge/docker_images-confluent-orange.svg?style=flat-square)](https://github.com/confluentinc/cp-docker-images)
[![Python](https://img.shields.io/badge/python-3.5+-blue.svg?style=flat-square)](https://www.python.org)



## Install

You will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/) to run it.


```bash
$ docker network create -d overlay --attachable kafka_default
```

All set!

## Quickstart

```bash
$ cd generator && docker build -t generator .
$ cd detector && docker build -t detector .

```

- Start the transaction generator and  detector (will run in the background):

```bash
$ docker stack deploy -c docker-compose.yml detgen
```

- Monitor transactions at the Kafdrop UI: http://kafdrop.localhost, assuming you previously set up kafka cluster with kafdrop UI

## Usage

Topics:

- `queuing.transactions`: raw generated transactions
- `streaming.transactions.other`: other currency transactions
- `streaming.transactions.btcusd`: BTC transactions



## Teardown

To stop the transaction generator and fraud detector:

```bash
$ docker stack rm detgen 

To stop the Kafka cluster

```bash
$ docker stacm rm kafka
```

To remove the Docker network:

```bash
$ docker network rm kafka_default
```

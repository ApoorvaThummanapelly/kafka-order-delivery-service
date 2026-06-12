# Kafka Order Delivery Service

A simple event-driven application built with Apache Kafka and Python to simulate an order delivery workflow. Apache Kafka is deployed and executed in a Docker container on a local desktop environment, enabling asynchronous communication between producer and consumer services.

## Architecture

Producer -> Kafka Topic -> Consumer

## Features

* Order creation and publishing
* Asynchronous message processing
* Kafka topic-based communication
* Kafka broker running in a Docker container

## Technologies

* Python
* Apache Kafka
* Docker
* kafka-python

## Run

Start Kafka in Docker:

```bash
docker compose up -d
```

Run the consumer:

```bash
python consumer.py
```

Run the producer:

```bash
python producer.py
```

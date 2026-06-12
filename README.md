# Kafka Order Delivery Service

A simple event-driven application built with Apache Kafka and Python.

## Architecture

Producer -> Kafka Topic -> Consumer

## Features

- Order creation and publishing
- Asynchronous message processing
- Kafka topic-based communication

## Technologies

- Python
- Apache Kafka
- Docker
- kafka-python

## Run

```bash
docker compose up -d
python consumer.py
python producer.py
```

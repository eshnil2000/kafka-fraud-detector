"""Produce transactions into a Kafka topic."""

import os
from time import sleep
import json

from kafka import KafkaProducer
from transactions import create_random_transaction

TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
KAFKA_BROKER_URL1 = os.environ.get('KAFKA_BROKER_URL1')
KAFKA_BROKER_URL2 = os.environ.get('KAFKA_BROKER_URL2')
KAFKA_BROKER_URL3 = os.environ.get('KAFKA_BROKER_URL3')
bootstrap_servers = [KAFKA_BROKER_URL1,KAFKA_BROKER_URL2,KAFKA_BROKER_URL3]

TRANSACTIONS_PER_SECOND = float(os.environ.get('TRANSACTIONS_PER_SECOND'))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    while True:
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction)  # DEBUG
        sleep(SLEEP_TIME)

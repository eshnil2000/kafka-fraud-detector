"""Example Kafka consumer."""

from random import choices, randint,choice
from string import ascii_letters, digits
import requests
import json
import os
from kafka import KafkaConsumer, KafkaProducer

#KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
KAFKA_BROKER_URL1 = os.environ.get('KAFKA_BROKER_URL1')
KAFKA_BROKER_URL2 = os.environ.get('KAFKA_BROKER_URL2')
KAFKA_BROKER_URL3 = os.environ.get('KAFKA_BROKER_URL3')
bootstrap_servers = [KAFKA_BROKER_URL1,KAFKA_BROKER_URL2,KAFKA_BROKER_URL3]
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
LEGIT_TOPIC = os.environ.get('LEGIT_TOPIC')
FRAUD_TOPIC = os.environ.get('FRAUD_TOPIC')


def _random_amount() -> float:
    """Return a random amount between 10.00 and 100.00."""
    return int(randint(1000, 10000) / 100)

def is_suspicious(transaction: dict) -> bool:
    """Determine whether a transaction is suspicious."""
    print(transaction)
    #side = choice(["buy", "sell"])
    #quantity= str(_random_amount())
    #price= str(_random_amount())
    #headers = {'Host':'crypto.localhost','Content-Type':'application/json'}
    headers = {'Content-Type':'application/json'}
    
    data_obj=transaction
    data=json.dumps(data_obj, separators=(',', ':'))

    #url= 'http://crypto:5000/order/new'
    url=  os.environ.get('ORDER_BOOK_URL')
    print(data)
    x = requests.post(url, data = data, headers=headers)
    return transaction['pair']=='BTC/USD'
    #return int(transaction['price']) >= 50
    #return transaction['amount'] >= 900


if __name__ == '__main__':
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    for message in consumer:
        transaction: dict = message.value
        topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        producer.send(topic, value=transaction)
        print(topic, transaction)  # DEBUG

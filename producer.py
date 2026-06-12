import json
import uuid

from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(producer_config)

order = {
    "order_id": str(uuid.uuid4()),
    "customer_name": "Rani",
    "item": "iphone"
}


def delivery_report(error, msg):
    if error:
        print("Delivery failed: ", {error})
    else:
        print("Delivery completed: ", msg.value().decode("utf-8"))
        print(f"Delivered msg to {msg.topic()} : partition {msg.partition()} at offset : {msg.offset()}")


event = json.dumps(order).encode("utf-8")
producer.produce(topic="orders", value=event, callback=delivery_report)
producer.flush()

import json

from confluent_kafka import Consumer

consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])
print("Consumer is subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Encountered error: {msg.error()}")
            continue

        event = msg.value().decode("utf-8")
        order = json.loads(event)
        print(f"Event is consumed for order : {order['order_id']} from user : {order['customer_name']}")

except KeyboardInterrupt:
    print("Stopping the consumer")

finally:
    consumer.close()
import json
import uuid

from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(producer_config)
user_name = input("Hi, Please enter your name: ")
print(f"Hi {user_name}, Here is the list of services we offer:")
print("1. Broadband "
      "2. Satellite "
      "3. IPTV "
      "4. OTT "
      "5. Mobile")
services_list = input("please enter the name in comma-separated values to add them to your cart: ")
order_item = []

for item in services_list.split(","):
    order_item.append(item)
order = {
    "order_id": str(uuid.uuid4()),
    "customer_name": user_name,
    "order_item": order_item
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

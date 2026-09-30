import json
from kafka import KafkaConsumer
from pymongo import MongoClient

# MongoDB Atlas Connection
# IMPORTANT: Replace the URI string below with your actual MongoDB Atlas connection string
mongo_uri = "mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client['ecommerce_streaming']
collection = db['orders']

# Kafka Consumer Configuration
consumer = KafkaConsumer(
    'orders',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest'
)

print("Starting Kafka Consumer. Listening for messages on 'orders' topic...")

# Continuous listening loop
for message in consumer:
    order_data = message.value
    
    # Insert the streaming event directly into MongoDB
    collection.insert_one(order_data)
    
    # Terminal output to verify data flow
    print(f"Inserted into MongoDB Atlas: Order {order_data.get('order_id')} | Status: {order_data.get('status')}")
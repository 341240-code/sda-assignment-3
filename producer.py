import csv
import json
import time
from kafka import KafkaProducer

# Configure the Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'], 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'orders'

print(f"Starting Kafka Producer. Sending data to topic: {topic_name}...")

# Infinite loop to keep the dashboard live while you take a screenshot
while True:
    try:
        with open('ecommerce_orders.csv', mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert numeric fields back to correct types for JSON
                row['quantity'] = int(row['quantity'])
                row['amount'] = float(row['amount'])
                
                # Send the message
                producer.send(topic_name, value=row)
                
                # Print terminal output to verify data flow
                print(f"Sent: {json.dumps(row)}")
                
                # Sleep for 3 seconds to simulate streaming data velocity
                time.sleep(3)
                
    except FileNotFoundError:
        print("Error: Make sure 'ecommerce_orders.csv' is in the exact same folder as this script!")
        break
# This script ingests data using Kafka and stores it in AWS S3
from kafka import KafkaConsumer
import boto3
import json

# AWS S3 Configuration
s3 = boto3.client('s3')
bucket_name = 'hotel-revenue-data'

# Kafka Configuration
consumer = KafkaConsumer(
    'hotel_bookings',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def ingest_data():
    for message in consumer:
        record = message.value
        file_name = f"booking_{record['id']}.json"
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(record))
        print(f"Ingested {file_name} to S3")

if __name__ == '__main__':
    ingest_data()

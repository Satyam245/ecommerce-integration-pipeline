import json
import time
import pandas as pd
from google.cloud import pubsub_v1

# Initialize the Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()

# Project and Topic details
project_id = "your-project-id"  # Replace with your actual project ID
topic_name = "your-topic-name"  # Replace with your actual topic name
topic_path = publisher.topic_path(project_id, topic_name)

# Callback function to handle the publishing results.
def callback(future):
    try:
        # Get the message_id after publishing.
        message_id = future.result()
        print(f"Published message with ID: {message_id}")
    except Exception as e:
        print(f"Error publishing message: {e}")

# Reading data from file
orders_df = pd.read_csv("olist_orders_dataset.csv")

try:
    while True:
        # Iterating orders_df data
        for index, row in orders_df.iterrows():
            json_data = {
                'order_id': row[0],
                'customer_id': row[1],
                'order_status': row[2],
                'order_purchase_timestamp': row[3],
                'order_approved_at': row[4],
                'order_delivered_carrier_date': row[5],
                'order_delivered_customer_date': row[6],
                'order_estimated_delivery_date': row[7]
            }
            # Serializing json_data dictionary to a json string
            json_data_str = json.dumps(json_data)

            future = publisher.publish(topic_path, data=json_data_str.encode('utf-8'))
            future.add_done_callback(callback)
            future.result()

            time.sleep(1)

except KeyboardInterrupt:
    print("Stopped")

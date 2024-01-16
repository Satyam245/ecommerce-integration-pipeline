# E-commerce Data Integration Pipeline

🚀 Welcome to the E-commerce Data Integration Pipeline project! This project leverages Python, GCP Pub/Sub, DataStax Cassandra, and Pandas to seamlessly integrate and process e-commerce data.

## Project Highlights:

- 📁 **Data Loading**: Load 'orders_data.csv' into Pandas for efficient data handling.

- 🌐 **GCP Pub/Sub Setup**: Set up GCP Pub/Sub for the 'ecommerce-orders' topic to enable communication between components.

- 🐍 **Python Producer**: Build a Python producer to smoothly publish data to the GCP Pub/Sub 'ecommerce-orders' topic.

- 🏗️ **Cassandra Table Setup**: Setup and create an 'orders' table in DataStax Cassandra to store processed data.

- 🔄 **Python Consumer**: Implement a Python consumer that seamlessly transforms data before inserting it into the Cassandra 'orders' table.

## Project Structure:

- `producer.py`: Python script for producing and publishing data to GCP Pub/Sub.

- `consumer.py`: Python script for consuming, transforming, and inserting data into DataStax Cassandra.

- `orders_data.csv`: Sample data file containing e-commerce orders.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Google Cloud Platform (GCP) Account**: Set up a GCP account and create a project. Obtain the necessary credentials for Pub/Sub.

- **DataStax Astra or Cassandra Database**: Set up a DataStax Astra or Cassandra cluster. Obtain the secure connect bundle and authentication credentials.

- **Python and Pip**: Ensure you have Python installed (version 3.x) along with pip, the package installer.

- **Pandas Library**: Install the Pandas library for efficient data handling:
  ```bash
  pip install pandas

import pika
import os
from dotenv import load_dotenv

load_dotenv()
# Truy cập các biến môi trường
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', '5672'))
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

# Thông tin kết nối
connection_parameters = pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials=pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD))

try:
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    # Tạo một queue
    channel.queue_declare(queue='hello')

    # Đưa một message vào queue
    channel.basic_publish(exchange='',
                           routing_key='hello',
                           body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
except pika.exceptions.AMQPConnectionError:
    print("Error connecting to RabbitMQ")
import pika
import json
import time

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('admin', 'admin')
        )
    )

    channel = connection.channel()

    # Declarar exchange tipo fanout (broadcast)
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    for i in range(25):
        message = {
            "event": "order_created",
            "order_id": 1234,
            "user": "John",
            "total": 250.00 * i
        }

        channel.basic_publish(
            exchange='logs',
            routing_key='',
            body=json.dumps(message)
        )

        print("📤 Mensaje enviado:", message)
        time.sleep(1)

    connection.close()


if __name__ == "__main__":
    main()
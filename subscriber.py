import pika

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials('admin', 'admin')
        )
    )

    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # Crear cola exclusiva temporal
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs', queue=queue_name)

    print("📥 Esperando mensajes...")

    def callback(ch, method, properties, body):
        print("✅ Mensaje recibido:", body.decode())

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


if __name__ == "__main__":
    main()
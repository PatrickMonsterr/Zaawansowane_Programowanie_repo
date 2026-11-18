import os
import time

import pika

QUEUE_NAME = "tasks"
RABBIT_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBIT_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))


def main():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT)
        )
    except pika.exceptions.AMQPConnectionError:
        print(
            f"Nie mozna polaczyc z RabbitMQ ({RABBIT_HOST}:{RABBIT_PORT}). "
            "Uruchom: docker compose up -d. "
            "Jesli broker dziala na innym porcie, ustaw RABBITMQ_PORT."
        )
        raise SystemExit(1)

    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)

    def callback(ch, method, properties, body):
        task = body.decode()
        print(f"Start zadania {task} (status: in_progress)")
        time.sleep(2)
        print(f"Koniec zadania {task} (status: done)")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    print("Consumer oczekuje na zadania...")
    channel.start_consuming()


if __name__ == "__main__":
    main()

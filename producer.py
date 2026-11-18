import os
import sys

import pika

QUEUE_NAME = "tasks"
RABBIT_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBIT_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))


def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
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

    for i in range(1, count + 1):
        message = f"task-{i}"
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print(f"Dodano zadanie: {message} (status: pending)")

    connection.close()
    print(f"Dodano {count} zadan.")


if __name__ == "__main__":
    main()

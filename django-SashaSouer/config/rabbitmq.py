import pika


def send_message(message):
    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Создание очереди
    channel.queue_declare(queue='my_queue')

    # Отправка сообщения
    channel.basic_publish(exchange='', routing_key='my_queue', body=message)

    # Закрытие соединения
    connection.close()

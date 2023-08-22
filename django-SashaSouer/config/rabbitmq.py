import pika


def send_message(message):
    # ����������� � RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # �������� �������
    channel.queue_declare(queue='my_queue')

    # �������� ���������
    channel.basic_publish(exchange='', routing_key='my_queue', body=message)

    # �������� ����������
    connection.close()

# # -*- coding: utf-8 -*-
# import pika
# import json
#
#
# def send_message(message):
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='parser_queue')
#     channel.basic_publish(exchange='', routing_key='parser_queue', body=json.dumps(message))
#     print(" [x] Sent message to parser_queue")
#     connection.close()

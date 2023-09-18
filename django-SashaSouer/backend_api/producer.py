import pika
import json
from backend_api.views import create_json_response_to_parser

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
try:
    channel = connection.channel()

    channel.queue_declare(queue='mainGPU', durable=True, arguments={"x-max-priority": 255})

    message = create_json_response_to_parser()
    json_message = message[0]
    json_data = json.dumps(json_message)
    channel.basic_publish(
        exchange='',
        routing_key='mainGPU',
        body=json_data,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
            priority=50
        ))
    print(" [x] Sent %r" % message[:50])
except Exception as e:
    print(e)
connection.close()

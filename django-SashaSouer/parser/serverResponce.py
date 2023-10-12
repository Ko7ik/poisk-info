# -*- coding: utf-8 -*-
import json

import requests
from configurate import localhost, admin_token

import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def get_data_from_server():
    url = f'http://{localhost}/api/create_json_response_to_parser/'  # Замените на адрес вашего представления
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        print('Сервер: - GET: Данные успешно отправлены парсеру')
        return data
    else:
        data = response.json()
        print(data)
        print('Сервер: - GET: Ошибка при отправки данных парсеру')
        return 1


def send_user_info_to_server(data):
    url = f'http://{localhost}/api/found_data/'
    token = f'Token {admin_token}'   # Передаём токен admin
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    # Преобразование словаря в JSON-строку
    json_data = json.dumps(data, ensure_ascii=False)

    # Вывод JSON-строки
    print(json_data)

    # Отправка JSON-строки на сервер
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print('Сервер: - POST: Данные успешно отправлены на сервер: ' + str(response.status_code))
    else:
        print('Сервер: - POST: Ошибка при отправке данных на сервер: ' + str(response.status_code))

# def send_user_info_to_server(data):
#     url = 'http://192.168.0.189:8000/api/found_data/'
#     token = 'Token f58c25e33da28c9dfe7ff38038a9864958c47dd5'   # Передаём токен admin
#     headers = {
#         'Authorization': token,
#         'Content-Type': 'application/json',
#     }
#     response = requests.post(url, json=data, headers=headers)
#
#     if response.status_code == 201:
#         print('Сервер: - POST: Данные успешно отправлены на сервер')
#     else:
#         print('Сервер: - POST: Ошибка при отправке данных на сервер')

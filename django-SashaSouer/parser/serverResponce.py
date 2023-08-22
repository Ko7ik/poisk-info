# -*- coding: utf-8 -*-
import requests


def get_data_from_server():
    url = 'http://192.168.0.189:8000/api/create_json_response_to_parser/'  # Замените на адрес вашего представления
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        print('Сервер: - GET: Данные успешно получены')
        return data
    else:
        data = response.json()
        print(data)
        print('Сервер: - GET: Ошибка при получении данных')
        return 1


def send_user_info_to_server(data):
    url = 'http://192.168.0.189:8000/api/found_data/'
    token = 'Token 55749880d1d95cceeecc3a0c3d52c2d8e7d86932'   # Передаём токен admin
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print('Сервер: - POST: Данные успешно отправлены на сервер')
    else:
        print('Сервер: - POST: Ошибка при отправке данных на сервер')

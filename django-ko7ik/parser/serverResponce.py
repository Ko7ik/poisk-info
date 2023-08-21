# -*- coding: utf-8 -*-
import requests


def get_data_from_server():
    url = 'http://192.168.0.189:8000/create_json_response_to_parser/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        data = response.json()
        print(data)
        print('Ошибка при получении данных')
        return 1


def send_user_info_to_server(data):
    url = 'http://192.168.0.189:8000/found_data/'
    response = requests.post(url, json=data,
                             # Токен для отправки данных на сервер
                             headers={"Authorization": "Token 8ee7aa4cb4db03326a027c6a70ec43468b1c627d"})

    if response.status_code == 201:
        print('Данные успешно отправлены на сервер. Код ответа: ', response.status_code)
    else:
        print('Ошибка при отправке данных на сервер. Код ответа: ', response.status_code)


def reg_parser_on_server(data_for_reg):
    url = 'http://192.168.0.189:8000/found_data/'
    response = requests.post(url, json=data_for_reg)
    if response.status_code == 201:
        print(response)
        return response
    else:
        print("Error ", response.status_code)


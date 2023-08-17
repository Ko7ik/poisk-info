# -*- coding: utf-8 -*-
import requests
def get_data_from_server():
    url = 'http://192.168.0.17:8000/serialize_and_save_to_json/'  # Замените на адрес вашего представления
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
    url = 'http://192.168.0.17:8000/found_data/'
    response = requests.post(url, json=data)

    if response.status_code == 201:
            print('Данные успешно отправлены на сервер')
    else:
            print('Ошибка при отправке данных на сервер')
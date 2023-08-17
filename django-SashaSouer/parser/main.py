# -*- coding: utf-8 -*-

from src.VkDriverTools import VkDriverTools
import requests


def get_data_from_server():
    url = 'http://192.168.0.189:8000/serialize_and_save_to_json/'  # Замените на адрес вашего представления
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Ошибка при получении данных')


if __name__ == '__main__':
    # config = jsonTools.parse('parser/config.example.json') # считывание пришедшего JSON файла
    vkDriverTools = VkDriverTools(get_data_from_server()) # разбиение данных из JSON файла по переменым
    vkDriverTools.login() # Авторизация
    vkDriverTools.get_feed()

    vkDriverTools.driver.close() # Закрытие бота

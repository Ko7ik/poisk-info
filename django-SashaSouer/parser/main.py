# -*- coding: utf-8 -*-
from parser.server_request import get_data_from_server
from src.VkDriverTools import VkDriverTools


<<<<<<< Updated upstream
def get_data_from_server():
    url = 'http://192.168.0.189:8000/serialize_and_save_to_json/'  # Замените на адрес вашего представления
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Ошибка при получении данных')

=======
>>>>>>> Stashed changes
if __name__ == '__main__':
    vkDriverTools = VkDriverTools(get_data_from_server()) # разбиение данных из JSON файла по переменым
    vkDriverTools.login() # Авторизация
    vkDriverTools.get_feed()
    vkDriverTools.driver.close() # Закрытие бота

# -*- coding: utf-8 -*-
from src.VkDriverTools import VkDriverTools
from multiprocessing import Pool
from backend_api.rabbitmq_consumer import consume_messages




def get_data(items):
    vkDriverTools = VkDriverTools()
    flag = 0
    for item in items[1]:
        vkDriverTools.raschlenenka(item)  # Получение POST
        print("Парсер: - Получил данные")
        if flag == 0:
            vkDriverTools.login()  # Авторизация
            print("Парсер: - Авторизовался")
            flag = 1
        if vkDriverTools.vk_last_id == 0:  # Проверка на обрабатывалась ли страница
            print("Парсер: - Выбрал get_start")
            vk = vkDriverTools.get_start  # Запуск парсера на обработку с первой записи
        else:
            print("Парсер: - Выбрал get_feed")
            vk = vkDriverTools.get_feed  # Запуск парсера на обработку с последней найденной записи
    vkDriverTools.driver.close()  # Закрытие бота
    print("Парсер: - Бот закрылся")


if __name__ == '__main__':
    # Реализация парсера через цикл и массив #
    # Получаем данные от сервера
    data = consume_messages()
    # Создаем два массива: один для данных с одинаковыми логинами, другой - для остальных данных
    sorted_data = {}

    for item in data:
        login = item.get('vk').get('auth').get('login')
        if login in sorted_data:
            sorted_data[login].append(item)
        else:
            sorted_data[login] = [item]

    # Теперь sorted_data содержит данные, сгруппированные по возрасту
    # Выводим данные для каждого возраста
    print(sorted_data)
    p = Pool(processes=len(sorted_data))
    p.map(get_data, sorted_data.items())
    print("Элементы закончились")


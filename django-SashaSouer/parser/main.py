# -*- coding: utf-8 -*-
from serverResponce import get_data_from_server
from src.VkDriverTools import VkDriverTools

if __name__ == '__main__':
    # Реализация парсера через цикл и массив #
    # Получаем данные от сервера
    data = get_data_from_server()
    # Создаем пустой массив для хранения элементов
    flag = 0
    vkDriverTools = VkDriverTools()
    # Добавляем каждый элемент JSON в массив
    for obj in data:
        vkDriverTools.raschlenenka(obj)  # Получение POST
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
            vk = vkDriverTools.get_feed # Запуск парсера на обработку с последней найденной записи
    vkDriverTools.driver.close()  # Закрытие бота
    print("Парсер: - Бот закрылся")

    print("Элементы закончились")

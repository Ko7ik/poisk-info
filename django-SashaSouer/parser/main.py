# -*- coding: utf-8 -*-
from serverResponce import get_data_from_server
from parser.VkDriverTools import VkDriverTools


if __name__ == '__main__':
    data = get_data_from_server()

    # Создаем пустой массив для хранения элементов
    array = []

    # Добавляем каждый элемент JSON в массив
    for obj in data:
        array.append(obj)

    while array:
        vkDriverTools = VkDriverTools(array[0])   # Получение POST
        print("Получил данные")
        vkDriverTools.login()  # Авторизация
        print("Авторизовался")

        if vkDriverTools.vk_last_id == 0:   # Проверка на обрабатывалась ли страница
            print("get_start")
            vkDriverTools.get_start()   # Запуск парсера на обработку с первой записи
        else:
            print("get_feed")
            vkDriverTools.get_feed()   # Запуск парсера на обработку с последней найденной записи

        vkDriverTools.driver.close()   # Закрытие бота
        print("Бот закрылся")
        array.pop(0)   # Удаляем первый элемент в списке
        print("Первый элемент массива удалён")
    print("Элементы закончились")

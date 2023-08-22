# -*- coding: utf-8 -*-
from parser.serverResponce import get_data_from_server
from parser.src.VkDriverTools import VkDriverTools
from parser.task import parse_data

if __name__ == '__main__':
    parse_data.delay()  # Запустить задачу парсинга асинхронно


# Реализация парсера через цикл и массив

    # data = get_data_from_server()
    #
    # # Создаем пустой массив для хранения элементов
    # array = []
    #
    # # Добавляем каждый элемент JSON в массив
    # for obj in data:
    #     array.append(obj)
    #
    # while array:
    #     vkDriverTools = VkDriverTools(array[0])  # Получение POST
    #     print("Парсер: - Получил данные")
    #     vkDriverTools.login()  # Авторизация
    #     print("Парсер: - Авторизовался")
    #
    #     if vkDriverTools.vk_last_id == 0:  # Проверка на обрабатывалась ли страница
    #         print("Парсер: - Выбрал get_start")
    #         vkDriverTools.get_start()  # Запуск парсера на обработку с первой записи
    #     else:
    #         print("Парсер: - Выбрал get_feed")
    #         vkDriverTools.get_feed()  # Запуск парсера на обработку с последней найденной записи
    #
    #     vkDriverTools.driver.close()  # Закрытие бота
    #     print("Парсер: - Бот закрылся")
    #     array.pop(0)  # Удаляем первый элемент в списке
    #     print("Первый элемент массива удалён")
    # print("Элементы закончились")

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

        # if vkDriverTools.vk_last_id == 0:   # Проверка на обрабатывалась ли страница
        #     vkDriverTools.get_start()
        #     print("get_start")
        # else:
        #     vkDriverTools.get_feed()
        #     print("get_feed")

        vkDriverTools.driver.close()   # Закрытие бота
        print("Бот закрылся")
        array.pop(0)   # Удаляем первый элемент в списке
        print("Первый элемент массива удалён")
    print("Элементы закончились")

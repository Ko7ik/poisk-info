# -*- coding: utf-8 -*-
from serverResponce import get_data_from_server
from parser.VkDriverTools import VkDriverTools


if __name__ == '__main__':
    vkDriverTools = VkDriverTools(get_data_from_server()) # Получение POST
    vkDriverTools.login()  # Авторизация

    if vkDriverTools.vk_last_id == 0: # Проверка на обрабатывалась ли страница
        vkDriverTools.get_start()
    else:
        vkDriverTools.get_feed()

    vkDriverTools.driver.close() # Закрытие бота

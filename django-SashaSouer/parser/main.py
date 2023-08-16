# -*- coding: utf-8 -*-

from src.JsonTools import JsonTools
from src.VkDriverTools import VkDriverTools
from datetime import datetime

if __name__ == '__main__':
    jsonTools = JsonTools() # создание объекта
    config = jsonTools.parse('parser/config.example.json') # считывание пришедшего JSON файла
    vkDriverTools = VkDriverTools(config) # разбиение данных из JSON файла по переменым
    vkDriverTools.login() # Авторизация
    post_start = vkDriverTools.get_start
    JsonTools.save(post_start)  # Сохранение постов в JSON
    #posts = vkDriverTools.get_feed # Получение постов
    #JsonTools.save(posts)  # Сохранение постов в JSON
    vkDriverTools.driver.close() # Закрытие бота

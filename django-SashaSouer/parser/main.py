# -*- coding: utf-8 -*-

from src.JsonTools import JsonTools
from src.VkDriverTools import VkDriverTools
from datetime import datetime


def formatPostToText(post):
    template = "\n[{0}] Новый пост!\nСсылка - {1}\nТекст - {2}\nСсылка на пикчу - {3}\nID - {4}"
    return template.format(post['time'], post['link'], post['text'] if len(post['text']) else "нет", post['image'] if len(post['image']) else "нет", post['id'])

if __name__ == '__main__':
    jsonTools = JsonTools()
    config = jsonTools.parse('config.example.json')
    vkDriverTools = VkDriverTools(config)
    vkDriverTools.login()

    posts = vkDriverTools.get_feed
    JsonTools.save(posts)
    vkDriverTools.driver.close()

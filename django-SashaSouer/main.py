import os
import webbrowser
import asyncio
from parser.src.JsonTools import JsonTools
from parser.src.VkDriverTools import VkDriverTools
from datetime import datetime

# RUNSERVER
async def runserver():
    path = 'C:/Users/tereh/PycharmProjects/poisk'
    os.chdir(path)
    os.system("python manage.py runserver")

# OPEN BROWSER
def openproject():
    webbrowser.open_new_tab("http://192.168.0.17:8000/index")

# EXECUTE PROGRAM
async def main():
    task1 = asyncio.create_task(runserver())
    openproject()
    await task1

# -*- coding: utf-8 -*-


def formatPostToText(post):
    template = "\n[{0}] Новый пост!\nСсылка - {1}\nТекст - {2}\nСсылка на пикчу - {3}\nID - {4}"
    return template.format(post['time'], post['link'], post['text'] if len(post['text']) else "нет", post['image'] if len(post['image']) else "нет", post['id'])

if __name__ == '__main__':
    jsonTools = JsonTools()
    config = jsonTools.parse('parser/config.example.json')
    vkDriverTools = VkDriverTools(config)
    vkDriverTools.login()

    posts = vkDriverTools.get_feed
    JsonTools.save(posts)
    vkDriverTools.driver.close()


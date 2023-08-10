from src.JsonTools import JsonTools
from src.VkDriverTools import VkDriverTools
from src.Cache import Cache
from datetime import datetime


def formatPostToText(post):
    template = "\n[{0}] Новый пост!\nСсылка - {1}\nТекст - {2}\nСсылка на пикчу - {3}\nID - {4}"
    return template.format(datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), post['link'], post['text'] if len(post['text']) else "нет", post['image'] if len(post['image']) else "нет", post['id'])

if __name__ == '__main__':
    jsonTools = JsonTools()
    config = jsonTools.parse('config.example.json')
    cache = Cache(config['paths']['cache_file'])
    vkDriverTools = VkDriverTools(config)
    vkDriverTools.login()

    posts = vkDriverTools.get_feed()
    for post in posts:
        cache.save(formatPostToText(post))
    vkDriverTools.driver.close()

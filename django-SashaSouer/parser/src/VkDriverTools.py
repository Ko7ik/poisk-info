# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime


class VkDriverTools:

    def __init__(self, config):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        # self.driver = webdriver.Chrome(config['paths']['chromedriver'])
        self.vk_login_url = config['vk']['urls']['login']
        self.vk_feed_url = config['vk']['urls']['feed']
        self.vk_login = config['vk']['auth']['login']
        self.vk_password = config['vk']['auth']['password']

    def get_driver(self):
        return self.driver

    @property
    def get_feed(self):
        self.driver.get(self.vk_feed_url)
        time.sleep(2)
        existing_data = []
        y_position = 2000
        k = -1
        flag = 1
        id_mass = []
        self.driver.execute_script(f'window.scrollTo(0, {y_position});')
        time.sleep(1)

        while flag == 1:
            k += 1
            # self.driver.execute_script(f'window.scrollTo(0, {y_position});')
            # self.driver.execute_script("arguments[0].scrollIntoView();", target_element)
            # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            posts = self.driver.find_elements(By.CLASS_NAME, '_post')

            for post in posts:
                image = []
                try:
                    # Выгрузка ID
                    id = post.find_element(By.CLASS_NAME, '_post').get_attribute('data-post-id')
                    flag_id = 0
                    for i in id_mass:
                        if id == i:
                            flag_id = 1
                            break
                    if flag_id != 1:
                        id_mass.append(id)
                        # Выгрузка времени публикации поста
                        try:
                            times = post.find_element(By.CLASS_NAME, 'PostHeaderSubtitle__item')
                            times = times.find_element(By.TAG_NAME, 'span').get_attribute('abs_time')
                            if times.find('сегодня') != -1:
                                times = times.replace('сегодня', str(datetime.date.today()))
                        except NoSuchElementException as e:
                            try:
                                times = post.find_element(By.CLASS_NAME, 'PostHeaderSubtitle__item').text
                            except NoSuchElementException as e:
                                pass

                        # Выгрузка ссылок картинок
                        urls = post.find_elements(By.CLASS_NAME, 'MediaGrid__thumb')
                        print(urls)
                        for url in urls:
                            try:
                                img = url.find_element(By.CLASS_NAME, 'MediaGrid__imageElement').get_attribute('src')
                                image.append(img)
                            except NoSuchElementException as e:
                                try:
                                    img = url.find_element(By.CLASS_NAME, 'MediaGrid__imageSingle').get_attribute('src')
                                    image.append(img)
                                except NoSuchElementException as e:
                                    pass
                        print(image)
                        # y_position += 1000
                        # self.driver.execute_script(f'window.scrollTo(0, {y_position});')

                        # Проверка на кнопку "показать еще"
                        try:
                            button = post.find_element(By.CLASS_NAME, 'PostTextMore').click()
                        except NoSuchElementException as e:
                            pass
                        element = post.find_element(By.CLASS_NAME, 'replies')
                        self.driver.execute_script("arguments[0].scrollIntoView();", element)
                        time.sleep(1)
                        # Выгрузка текста из поста
                        text = post.find_element(By.CLASS_NAME, 'wall_post_text')
                        text = text.text

                        # передача для создания итогого файла
                        data = {
                            "time": times,
                            "image": image,
                            "text": text,
                            "id": id,
                            "link": "https://vk.com/wall{}".format(id)
                        }
                        existing_data.append(data)
                        if k == 1:
                            flag = 0
                except NoSuchElementException as e:
                    pass
        return existing_data

    def login(self):
        self.driver.get(self.vk_login_url)
        email_input = self.driver.find_element(By.ID, 'index_email')
        email_input.clear()
        email_input.send_keys(self.vk_login)
        email_input.send_keys(Keys.ENTER)
        time.sleep(10)
        try:
            slize = self.driver.find_element(By.CSS_SELECTOR,
                                             '.vkc__PureButton__button.vkc__Link__link.vkc__Link__primary'
                                             '.vkc__Bottom__switchToPassword').click()
            time.sleep(5)
        except NoSuchElementException as e:
            pass
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(self.vk_password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

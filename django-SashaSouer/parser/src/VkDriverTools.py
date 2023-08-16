# -*- coding: utf-8 -*-

import string
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import requests


class VkDriverTools:

    def __init__(self, config):  # запуск драйвера и выгрузка данных из JSON
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        # self.driver = webdriver.Chrome(config['paths']['chromedriver'])
        self.id_task = int(config['vk']['task']['id_task'])
        self.vk_login_url = config['vk']['urls']['login']
        self.vk_feed_url = config['vk']['urls']['feed']
        self.vk_login = config['vk']['auth']['login']
        self.vk_password = config['vk']['auth']['password']
        self.vk_last_id = int(config['vk']['task']['id_last_post'])
        self.vk_text_search = config['vk']['task']['text']
        result = ''.join(filter(lambda x: x not in string.punctuation, self.vk_text_search))
        self.vk_text_search = result.split()

    def send_user_info_to_server(self, data):
        # data =  {
        #     "id_task": 1,
        #     "date_post": "421412",
        #     "img": "",
        #     "found_text": "412412",
        #     "id_post": "124124",
        #     "link": "https://vk.com/wall{id}"
        # }
        url = 'http://192.168.0.17:8000/found_data/'
        response = requests.post(url, json=data)

        if response.status_code == 201:
            print('Данные успешно отправлены на сервер')
        else:
            print('Ошибка при отправке данных на сервер')

    def get_driver(self):
        return self.driver

    @property
    def get_start(self):  # функция непосредственно парсера стены группы
        self.driver.get(self.vk_feed_url)  # переход на страницу таска
        time.sleep(2)
        existing_data = []
        id_mass = set()

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # скролим до первой записи
        time.sleep(1)

        while True:

            posts = self.driver.find_elements(By.CLASS_NAME, '_post')  # поиск всех постов, которые прогрузились

            for post in posts:
                try:
                    # Выгрузка ID
                    id = int(post.get_attribute('data-post-id').replace('-', '').replace('_', ''))
                    if id in id_mass:
                        continue
                    id_mass.add(id)

                    # Выгрузка времени публикации поста
                    try:
                        times_element = post.find_element(By.CLASS_NAME, 'PostHeaderSubtitle__item')
                        times = times_element.find_element(By.TAG_NAME, 'span').get_attribute('abs_time')
                        if 'сегодня' in times:
                            times = times.replace('сегодня', str(datetime.date.today()))
                    except NoSuchElementException:
                        times = post.find_element(By.CLASS_NAME, 'PostHeaderSubtitle__item').text

                    # Выгрузка ссылок картинок
                    image = []
                    urls = post.find_elements(By.CLASS_NAME, 'MediaGrid__thumb')
                    for url in urls:
                        try:
                            img = url.find_element(By.CLASS_NAME, 'MediaGrid__imageElement').get_attribute('src')
                            image.append(img)
                        except NoSuchElementException:
                            pass

                    # Проверка на кнопку "показать еще"
                    try:
                        button = post.find_element(By.CLASS_NAME, 'PostTextMore').click()
                    except NoSuchElementException:
                        pass
                    except ElementClickInterceptedException:
                        pass

                    element = post.find_element(By.CLASS_NAME, 'replies')  # поиск элемента для скролла
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)  # скролл
                    time.sleep(1)

                    # Выгрузка текста из поста
                    text = post.find_element(By.CLASS_NAME, 'wall_post_text').text
                    id_str = str(id)
                    # передача для создания итогого файла
                    data = {
                        "id_task": self.id_task,
                        "date_post": times,
                        "img": image,
                        "found_text": text,
                        "id_post": id_str,
                        "link": f"https://vk.com/wall{id}"
                    }
                    self.send_user_info_to_server(data)
                    time.sleep(3)
                    existing_data.append(data)

                except NoSuchElementException:
                    pass

            if len(existing_data) >= 2:
                break


    @property
    def get_feed(self):  # функция непосредственно парсера стены группы

        def find_matching_words_in_string(text, keywords):
            result = ''.join(filter(lambda x: x not in string.punctuation, text))
            words = result.split()  # Разделение строки на слова

            for word in words:
                if word in keywords:
                    return 1

        self.driver.get(self.vk_feed_url)  # переход на страницу таска
        time.sleep(2)
        existing_data = []
        id_mass = set()
        flag = 0

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # скролим до первой записи
        time.sleep(1)

        while True:

            posts = self.driver.find_elements(By.CLASS_NAME, '_post')  # поиск всех постов, которые прогрузились

            for post in posts:

                try:
                    # Выгрузка ID
                    id = int(post.get_attribute('data-post-id').replace('-', '').replace('_', ''))
                    if id == self.vk_last_id:
                        flag = 1
                        break
                    if id in id_mass:
                        continue
                    id_mass.add(id)

                    # Выгрузка времени публикации поста
                    try:
                        times_element = post.find_element(By.CLASS_NAME, 'PostHeaderSubtitle__item')
                        times = times_element.find_element(By.TAG_NAME, 'span').get_attribute('abs_time')
                        if 'сегодня' in times:
                            times = times.replace('сегодня', str(datetime.date.today()))
                    except NoSuchElementException:
                        times = post.find_element(By.CLASS_NAME, 'PostHeaderSubtitle__item').text

                    # Выгрузка ссылок картинок
                    image = []
                    urls = post.find_elements(By.CLASS_NAME, 'MediaGrid__thumb')
                    for url in urls:
                        try:
                            img = url.find_element(By.CLASS_NAME, 'MediaGrid__imageElement').get_attribute('src')
                            image.append(img)
                        except NoSuchElementException:
                            pass

                    # Проверка на кнопку "показать еще"
                    try:
                        button = post.find_element(By.CLASS_NAME, 'PostTextMore').click()
                    except NoSuchElementException:
                        pass
                    except ElementClickInterceptedException:
                        pass

                    element = post.find_element(By.CLASS_NAME, 'replies')  # поиск элемента для скролла
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)  # скролл
                    time.sleep(1)

                    # Выгрузка текста из поста
                    text = post.find_element(By.CLASS_NAME, 'wall_post_text').text
                    id_str = str(id)
                    if find_matching_words_in_string(text, self.vk_text_search) == 1:

                        # передача для создания итогого файла
                        data = {
                            "id_task": self.id_task,
                            "date_post": times,
                            "img": image,
                            "found_text": text,
                            "id_post": id_str,
                            "link": f"https://vk.com/wall{id}"
                        }
                        self.send_user_info_to_server(data)
                        time.sleep(3)
                        existing_data.append(data)

                except NoSuchElementException:
                    pass

            if flag == 1:
                break

        return existing_data

    def login(self):  # Авторизация бота
        self.driver.get(self.vk_login_url)  # переход на страницу авторизации
        # поиск поля Введите логин или номер телефона, ввод данных и нажатие на кнопку входа
        email_input = self.driver.find_element(By.ID, 'index_email')
        email_input.clear()
        email_input.send_keys(self.vk_login)
        email_input.send_keys(Keys.ENTER)
        time.sleep(10)

        # поиск кнопки войти по паролю, если это необходимо
        try:
            slize = self.driver.find_element(By.CSS_SELECTOR,
                                             '.vkc__PureButton__button.vkc__Link__link.vkc__Link__primary'
                                             '.vkc__Bottom__switchToPassword').click()
            time.sleep(5)
        except NoSuchElementException as e:
            pass

        # поиск поля Введите пароль, нажатие на кнопку входа
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(self.vk_password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

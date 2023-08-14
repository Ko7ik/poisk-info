# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime


class VkDriverTools:

    def __init__(self, config): # запуск драйвера и выгрузка данных из JSON
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
    def get_feed(self): # функция непосредственно парсера стены группы
        self.driver.get(self.vk_feed_url) # переход на страницу таска
        time.sleep(2)
        existing_data = []
        id_mass = set()

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # скролим до первой записи
        time.sleep(1)

        while True:

            posts = self.driver.find_elements(By.CLASS_NAME, '_post') # поиск всех постов, которые прогрузились

            for post in posts:
                try:
                    # Выгрузка ID
                    id = post.get_attribute('data-post-id')
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

                    element = post.find_element(By.CLASS_NAME, 'replies') # поиск элемента для скролла
                    self.driver.execute_script("arguments[0].scrollIntoView();", element) # скролл
                    time.sleep(1)

                    # Выгрузка текста из поста
                    text = post.find_element(By.CLASS_NAME, 'wall_post_text').text

                    # передача для создания итогого файла
                    data = {
                        "time": times,
                        "image": image,
                        "text": text,
                        "id": id,
                        "link": f"https://vk.com/wall{id}"
                    }
                    existing_data.append(data)

                except NoSuchElementException:
                    pass

            if len(existing_data) >= 25:
                break

        return existing_data

    def login(self): # Авторизация бота
        self.driver.get(self.vk_login_url) # переход на страницу авторизации
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

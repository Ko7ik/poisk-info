# -*- coding: utf-8 -*-
import re
import string
import time

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import FakeUserAgent
import datetime
import json

from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from parser.serverResponce import send_user_info_to_server


class VkDriverTools:

    def __init__(self):  # запуск драйвера и выгрузка данных из JSON
        service = Service()
        useragent = FakeUserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={useragent.random}')  # рандомный User_Agent
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.headless = True
        self.driver = webdriver.Chrome(service=service, options=options)

    def raschlenenka(self, config):  # функция расчленения JSON файла
        self.id_task = int(config['vk']['task']['id_task'])
        self.vk_login_url = config['vk']['urls']['login']
        self.vk_feed_url = config['vk']['urls']['feed']
        self.vk_login = config['vk']['auth']['login']
        self.vk_password = config['vk']['auth']['password']
        self.vk_last_id = int(config['vk']['task']['id_last_post'])
        self.vk_text_search = config['vk']['task']['text']
        self.vk_status = config['vk']['task']['status']
        result = ''.join(filter(lambda x: x not in string.punctuation, self.vk_text_search))
        self.vk_text_search = result.split()

    def get_driver(self):
        return self.driver

    def find_matching_words_in_string(self, text, keywords):  # поиск ключевых слов в тексте, пока по тупому
        result = ''.join(filter(lambda x: x not in string.punctuation, text))
        words = result.split()  # Разделение строки на слова

        for word in words:
            if word in keywords:
                return 1

    def parsering(self, post):
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
        if not urls:
            urls = post.find_elements(By.CLASS_NAME, 'ui_gallery_item')
            for url in urls:
                try:
                    img = url.find_element(By.CLASS_NAME,
                                           'PhotoPrimaryAttachment__imageElement.PhotoPrimaryAttachment__imageElement--inCarousel').get_attribute(
                        'src')
                    image.append(img)
                except NoSuchElementException:
                    pass
        else:
            for url in urls:
                try:
                    img = url.find_element(By.CLASS_NAME, 'MediaGrid__imageElement').get_attribute('src')
                    try:
                        vid = url.find_element(By.CLASS_NAME, 'MediaGrid__interactive').get_attribute('href')
                        match = re.search("video", str(vid))
                        if match:
                            image.append(vid)
                        else:
                            image.append(img)
                    except NoSuchElementException:
                        try:
                            vid = post.find_element(By.CLASS_NAME, 'page_post_sized_thumbs.clear_fix').get_attribute(
                                'href')
                            print(vid)
                        except NoSuchElementException:
                            pass
                except NoSuchElementException:
                    pass
        # Проверка на кнопку "показать еще"
        try:
            post.find_element(By.CLASS_NAME, 'PostTextMore').click()
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            pass

        element = post.find_element(By.CLASS_NAME, 'replies')  # поиск элемента для скролла
        self.driver.execute_script("arguments[0].scrollIntoView();", element)  # скролл

        # Выгрузка текста из поста
        text = post.find_element(By.CLASS_NAME, 'wall_post_text').text
        id_str = str(id)

        # Видео

        if self.find_matching_words_in_string(text, self.vk_text_search) == 1:
            # передача для создания итогого файла
            data = {
                "id_task": self.id_task,
                "date_post": times,
                "img": image,
                "found_text": text,
                "id_post": id_str,
                "link": f"https://vk.com/wall{id}"
            }

            send_user_info_to_server(data)
            return data

    @property
    def get_start(self):  # функция непосредственно парсера стены группы
        print("get_start: - Начал парсить")
        self.driver.get(self.vk_feed_url)  # переход на страницу таска
        existing_data = []
        id_mass = set()

        # Парсинг названия профиля или группы
        try:
            name = self.driver.find_element(By.ID, 'owner_page_name').text
            print(name)
        except NoSuchElementException:
            try:
                name = self.driver.find_element(By.CLASS_NAME, 'page_name').text
                print(name)
            except NoSuchElementException:
                pass

        # Проверка на закрыта группа или нет
        try:
            ex = self.driver.find_element(By.CLASS_NAME, 'redesigned-group-closed-block__text').text
            print(ex)
            print('Статус таска 4')
            try:
                button_invaite = self.driver.find_element(By.CLASS_NAME,
                                                          'FlatButton.FlatButton--primary.FlatButton--size-m.redesigned-group-action')
                if button_invaite.text == "Подать заявку":
                    self.driver.find_element(By.CLASS_NAME,
                                             'FlatButton.FlatButton--primary.FlatButton--size-m.redesigned-group-action').click()
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            try:
                ex1 = self.driver.find_element(By.CLASS_NAME,
                                               'ClosedProfileBlock-module__title--AAudM.vkuiTitle--level-3.vkuiTypography--normalize.vkuiTypography--weight-2').text
                print(ex1)
                print("Статус таска 6")
                try:
                    button_invaite = self.driver.find_element(By.CLASS_NAME, 'vkuiButton__content')
                    if button_invaite.text == "Добавить в друзья":
                        self.driver.find_element(By.CLASS_NAME, 'vkuiButton__content').click()
                except NoSuchElementException:
                    pass
                except ElementClickInterceptedException:
                    pass
            except NoSuchElementException:
                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # скролим до первой записи

                while True:

                    posts = self.driver.find_elements(By.CLASS_NAME, '_post')  # поиск всех постов, которые прогрузились

                    for post in posts:
                        try:
                            # Выгрузка ID
                            id = int(post.get_attribute('data-post-id').replace('-', '').replace('_', ''))
                            if id in id_mass:
                                continue
                            id_mass.add(id)
                            existing_data.append(self.parsering(post))
                        except NoSuchElementException:
                            pass
                    if len(existing_data) >= 2:
                        print(self.vk_status)
                        print(max(id_mass))
                        break

    @property
    def get_feed(self):  # функция непосредственно парсера стены группы
        print('Начал парсить через get_feed')

        self.driver.get(self.vk_feed_url)  # переход на страницу таска
        id_mass = set()
        flag = 0

        # Парсинг названия профиля или группы
        try:
            name = self.driver.find_element(By.ID, 'owner_page_name').text
            print(name)
        except NoSuchElementException:
            try:
                name = self.driver.find_element(By.CLASS_NAME, 'page_name').text
                print(name)
            except NoSuchElementException:
                pass

        # Проверка на закрыта группа или нет
        try:
            ex = self.driver.find_element(By.CLASS_NAME, 'redesigned-group-closed-block__text').text
            print(ex)
            print('Статус таска 4')
            try:
                button_invaite = self.driver.find_element(By.CLASS_NAME,
                                                          'FlatButton.FlatButton--primary.FlatButton--size-m.redesigned-group-action')
                if button_invaite.text == "Подать заявку":
                    self.driver.find_element(By.CLASS_NAME,
                                             'FlatButton.FlatButton--primary.FlatButton--size-m.redesigned-group-action').click()
            except NoSuchElementException:
                pass
            except ElementClickInterceptedException:
                pass
        except NoSuchElementException:
            try:
                ex = self.driver.find_element(By.CLASS_NAME,
                                              'ClosedProfileBlock-module__title--AAudM.vkuiTitle--level-3.vkuiTypography--normalize.vkuiTypography--weight-2')
                print(ex.text)
                print("Статус таска 6")
                try:
                    button_invaite = self.driver.find_element(By.CLASS_NAME, 'vkuiButton__content')
                    if button_invaite.text == "Добавить в друзья":
                        self.driver.find_element(By.CLASS_NAME, 'vkuiButton__content').click()
                except NoSuchElementException:
                    pass
                except ElementClickInterceptedException:
                    pass
            except NoSuchElementException:
                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # скролим до первой записи

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
                            self.parsering(post)
                        except NoSuchElementException:
                            pass
                    if flag == 1:
                        print(self.vk_status)
                        print(max(id_mass))
                        break

    def login(self):  # Авторизация бота
        self.driver.get(self.vk_login_url)  # переход на страницу авторизации
        # поиск поля Введите логин или номер телефона, ввод данных и нажатие на кнопку входа
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.ID, 'index_email')))
        email_input = self.driver.find_element(By.ID, 'index_email')
        email_input.clear()
        email_input.send_keys(self.vk_login)
        email_input.send_keys(Keys.ENTER)
        time.sleep(1)
        # поиск кнопки войти по паролю, если это необходимо
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     '.vkc__PureButton__button.vkc__Link__link.vkc__Link__primary'
                                     '.vkc__Bottom__switchToPassword').click()
        except NoSuchElementException:
            pass

        # поиск поля Введите пароль, нажатие на кнопку входа
        time.sleep(3)
        try:
            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.clear()
            password_input.send_keys(self.vk_password)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5)
        except NoSuchElementException:
            print("Статус таска 5")

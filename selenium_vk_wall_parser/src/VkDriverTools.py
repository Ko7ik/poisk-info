# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.action_chains import ActionChains
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
        wall_data = []

        # Move down page to bottom
        y_position = 400

        # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        k = -1
        flag = 1
        # y_position += 500
        time.sleep(1)
        # self.driver.execute_script(f'window.scrollTo(0, {y_position});')
        while flag == 1:
            k += 1
            # self.driver.execute_script("arguments[0].scrollIntoView();", target_element)
            y_position1 = y_position
            y_position += 600
            self.driver.execute_script(f'window.scrollTo(0, {y_position});')
            #self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            time.sleep(5)
            posts = self.driver.find_elements(By.CLASS_NAME, '_post')
            for post in posts:
                image = []
                try:
                    # Выгрузка ID
                    id = post.find_element(By.CLASS_NAME, '_post').get_attribute('data-post-id')

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
                    button = post.find_element(By.CLASS_NAME, 'PostTextMore').click()
                    y_position += 1000
                    self.driver.execute_script(f'window.scrollTo(0, {y_position});')
                    # Проверка на кнопку "показать еще"
                    try:
                        # Находим элемент, который перекрывается
                        intercepting_element = post.find_element(By.CLASS_NAME, 'HeaderNav__item')

                        # Находим целевой элемент для клика
                        target_element = post.find_element(By.CLASS_NAME, 'PostTextMore')

                        # Создаем экземпляр класса ActionChains
                        actions = ActionChains(self.driver)

                        # Наводим курсор на элемент, который перекрывает
                        actions.move_to_element(intercepting_element)

                        # Кликаем по целевому элементу
                        #actions.click(target_element).perform()


                        # time.sleep(5)
                    except NoSuchElementException as e:
                        pass

                    # Выгрузка текста из поста
                    text = post.find_element(By.CLASS_NAME, 'wall_post_text')
                    text = text.text.replace('\u20bd', '')
                    print(text)

                    # передача для создания итогого файла
                    wall_data.append({"time": times, "image": 'im', "text": text, "id": id,
                                      "link": "https://vk.com/wall{}".format(id)})
                    if k == 1:
                        flag = 0
                except NoSuchElementException as e:
                    pass
        return wall_data

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

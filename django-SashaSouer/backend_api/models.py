from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from rest_framework.authtoken.models import Token
from django.db import models


class VkParserData(models.Model):
    """Таблица с данными для авторизации парсера"""
    id_data = models.AutoField(primary_key=True)
    login = models.CharField(verbose_name="Логин")
    password = models.CharField(verbose_name="Пароль")

    def __str__(self):
        return self.login


class StatusTask(models.Model):
    """Таблица для статусов тасков"""
    id_status = models.AutoField(primary_key=True)
    status = models.CharField(verbose_name="Статус таска")

    def __str__(self):
        return self.status


class SocialNetwork(models.Model):
    """Таблица для выбора соцсети"""
    id_social = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Название соцсети")

    def __str__(self):
        return self.name


class UserToken(Token):
    user_identifier = models.IntegerField()


class Task(models.Model):
    """Таблица с тасками для поиска"""
    id_task_name = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    social_net = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE, verbose_name="Социальная сеть")
    search_text = models.CharField(verbose_name="Искомый текст")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    vk_parser_data_id = models.ForeignKey(VkParserData, on_delete=models.CASCADE, verbose_name="Данные для парсера",
                                          default=1)
    url_source = models.URLField(verbose_name="URL цели")
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE, verbose_name="Статус таска", default=1)
    id_last_post = models.CharField(verbose_name="id последнего поста", default="0")

    def __str__(self):
        return self.url_source


class FoundData(models.Model):
    """Таблица для найденных по таскам данных"""
    id_found_data = models.AutoField(primary_key=True)
    name_source = models.CharField(verbose_name="Цель поиска", blank=True, null=True)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Таск")
    id_post = models.CharField(verbose_name="ID поста")
    date_post = models.CharField(verbose_name="Дата публикации")
    img = models.JSONField(verbose_name="Фотография", blank=True, null=True)
    video = ArrayField(models.CharField(verbose_name="Видео"), blank=True, null=True)
    found_text = models.TextField(verbose_name="Найденный текст")
    link = models.CharField(verbose_name="Ссылка на публикацию")



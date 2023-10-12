from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from rest_framework.authtoken.models import Token
from django.db import models


# ДОБАВИТЬ НАЗВАНИЕ ТАБЛИЦ И СТРОК

class VkParserData(models.Model):
    """Таблица с данными для авторизации парсера"""
    id_data = models.AutoField(primary_key=True, db_column='id_data')
    login = models.CharField(verbose_name="Логин", db_column='login')
    password = models.CharField(verbose_name="Пароль", db_column='password')

    def __str__(self):
        return self.login

    class Meta:
        db_table = 'vk_parser_data'  # Можно указать имя таблицы вручную


class StatusTask(models.Model):
    """Таблица для статусов тасков"""
    id_status = models.AutoField(primary_key=True, db_column='id_status')
    status = models.CharField(verbose_name="Статус таска", db_column='status')

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'status_task'  # Можно указать имя таблицы вручную


class SocialNetwork(models.Model):
    """Таблица для выбора соцсети"""
    id_social = models.AutoField(primary_key=True, db_column='id_social')
    name = models.CharField(verbose_name="Название соцсети", db_column='name')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'social_network'  # Можно указать имя таблицы вручную


class UserToken(Token):
    user_identifier = models.IntegerField()


class Task(models.Model):
    """Таблица с тасками для поиска"""
    id_task_name = models.AutoField(primary_key=True, db_column='id_task_name')
    user_id = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, db_column='user_id')
    social_net = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE, verbose_name="Социальная сеть",
                                   db_column='social_net')
    search_text = models.CharField(verbose_name="Искомый текст", db_column='search_text')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", db_column='date')
    vk_parser_data_id = models.ForeignKey(VkParserData, on_delete=models.CASCADE, verbose_name="Данные для парсера",
                                          default=1, db_column='vk_parser_data_id')
    url_source = models.URLField(verbose_name="URL цели", db_column='url_source')
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE, verbose_name="Статус таска", default=1,
                               db_column='status')
    id_last_post = models.CharField(verbose_name="id последнего поста", default="0", db_column='id_last_post')

    class Meta:
        db_table = 'task'  # Можно указать имя таблицы вручную


class FoundData(models.Model):
    """Таблица для найденных по таскам данных"""
    id_found_data = models.AutoField(primary_key=True, db_column='id_found_data')
    name_source = models.CharField(verbose_name="Цель поиска", blank=True, null=True, db_column='name_source')
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Таск", db_column='id_task')
    id_post = models.CharField(verbose_name="ID поста", db_column='id_post')
    date_post = models.CharField(verbose_name="Дата публикации", db_column='date_post')
    img = models.JSONField(verbose_name="Фотография", blank=True, null=True, db_column='img')
    video = ArrayField(models.CharField(verbose_name="Видео"), blank=True, null=True, db_column='video')
    found_text = models.TextField(verbose_name="Найденный текст", db_column='found_text')
    link = models.CharField(verbose_name="Ссылка на публикацию", db_column='link')

    class Meta:
        db_table = 'found_data'

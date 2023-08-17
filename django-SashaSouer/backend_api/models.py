from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.postgres.fields import ArrayField


class UserProfile(models.Model):
    """Таблица для пользователей из Django"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class VkParserData(models.Model):
    """Таблица с данными для авторизации парсера"""
    login = models.CharField(verbose_name="Логин")
    password = models.CharField(verbose_name="Пароль")

    def __str__(self):
        return self.login


class StatusTask(models.Model):
    """Таблица для статусов тасков"""
    status = models.CharField(verbose_name="Статус таска")

    def __str__(self):
        return self.status


class SocialNetwork(models.Model):
    """Таблица для выбора соцсети"""
    name = models.CharField(verbose_name="Название соцсети")

    def __str__(self):
        return self.name


class Task(models.Model):
    """Таблица с тасками для поиска"""
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь")
    social_net = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE, verbose_name="Социальная сеть")
    search_text = models.CharField(verbose_name="Искомый текст")
    date = models.DateTimeField(verbose_name="Дата создания")
    vk_parser_data_id = models.ForeignKey(VkParserData, on_delete=models.CASCADE, verbose_name="Данные для парсера")
    url_group = models.URLField(verbose_name="URL Группы")
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE, verbose_name="Статус таска")
    numbers_of_posts = models.IntegerField(default=0, verbose_name="Количество постов")
    id_last_post = models.CharField(verbose_name="id последнего поста")

    def __str__(self):
        return self.url_group

    def update_numbers_of_posts(self):
        self.numbers_of_posts = self.FooundData.count()
        self.save()


class FoundData(models.Model):
    """Таблица для найденных по таскам данных"""
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Таск")
    id_post = models.CharField(verbose_name="ID поста")
    date_post = models.CharField(verbose_name="Дата публикации")
    img = ArrayField(models.CharField(verbose_name="Фотография"), blank=True, null=True)
    found_text = models.TextField(verbose_name="Найденный текст")
    link = models.CharField(verbose_name="Ссылка на публикацию")

    def __str__(self):
        return self.id_task

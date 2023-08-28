from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework.authtoken.models import Token


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


class UserToken(Token):
    user_identifier = models.IntegerField()


# class CountOfPosts(models.Model):
#     """Таблица для подсчёта количества постов"""
#     count = models.IntegerField()


class Task(models.Model):
    """Таблица с тасками для поиска"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    social_net = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE, verbose_name="Социальная сеть")
    search_text = models.CharField(verbose_name="Искомый текст")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    vk_parser_data_id = models.ForeignKey(VkParserData, on_delete=models.CASCADE, verbose_name="Данные для парсера",
                                          default=1)
    url_group = models.URLField(verbose_name="URL Группы")
    status = models.ForeignKey(StatusTask, on_delete=models.CASCADE, verbose_name="Статус таска", default=1)
    # numbers_of_posts = models.IntegerField(default=0, verbose_name="Количество постов")
    id_last_post = models.CharField(verbose_name="id последнего поста", default="1991591211346")

    def __str__(self):
        return self.url_group


# class PostCount(models.ForeignKey):
#     post = models.OneToOneField(Task, on_delete=models.SET_NULL, related_name='post_count')
#     record_count = models.ForeignKey(CountOfPosts, on_delete=models.DO_NOTHING)


class FoundData(models.Model):
    """Таблица для найденных по таскам данных"""
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Таск")
    id_post = models.CharField(verbose_name="ID поста")
    date_post = models.CharField(verbose_name="Дата публикации")
    img = ArrayField(models.CharField(verbose_name="Фотография"), blank=True, null=True)
    found_text = models.TextField(verbose_name="Найденный текст")
    link = models.CharField(verbose_name="Ссылка на публикацию")

# class SearchData(models.Model):
#     """Таблица с данными для поиска"""
#     url_group = models.URLField(max_length=200, null=False, blank=True, verbose_name="URL Группы")
#     search_string = models.CharField(max_length=200, null=False, blank=True, verbose_name="Искомая строка")
#
#     def __str__(self):
#         return f'{self.url_group}'
#
#     class Meta:
#         verbose_name = 'Данные для поиска'
#         verbose_name_plural = 'Данные для поиска'
#
#
# class FoundData(models.Model):
#     """Таблица с данными для вывода"""
#     time = models.CharField(max_length=50, blank=True, verbose_name="Дата и время публикации")
#     image = models.FileField(upload_to='img/', verbose_name="Изображения")
#     text = models.TextField(null=True, verbose_name='Найденные данные')
#     id_post = models.CharField(max_length=20, blank=True, verbose_name="ID поста")
#     link = models.ForeignKey('SearchData', on_delete=models.PROTECT, null=True, verbose_name="URL Группы")
#
#     def __str__(self):
#         return f'{self.link}'
#
#     class Meta:
#         verbose_name = 'Результат поиска'
#         verbose_name_plural = 'Результаты поиска'

from django.db import models


class SearchData(models.Model):
    """Таблица с данными для поиска"""
    url_group = models.URLField(max_length=200, null=False, blank=True, verbose_name="URL Группы")
    search_string = models.CharField(max_length=200, null=False, blank=True, verbose_name="Искомая строка")

    def __str__(self):
        return f'{self.url_group}'

    class Meta:
        verbose_name = 'Данные для поиска'
        verbose_name_plural = 'Данные для поиска'


class FoundData(models.Model):
    """Таблица с данными для вывода"""
    time = models.CharField(max_length=50, blank=True, verbose_name="Дата и время публикации")
    image = models.FileField(upload_to='img/', verbose_name="Изображения")
    text = models.TextField(null=True, verbose_name='Найденные данные')
    id_post = models.CharField(max_length=20, blank=True, verbose_name="ID поста")
    link = models.ForeignKey('SearchData', on_delete=models.PROTECT, null=True, verbose_name="URL Группы")

    def __str__(self):
        return f'{self.link}'

    class Meta:
        verbose_name = 'Результат поиска'
        verbose_name_plural = 'Результаты поиска'

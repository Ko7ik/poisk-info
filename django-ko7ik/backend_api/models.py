from django.db import models

# с большой буквы навания классов camelcase SearchData
class search_data(models.Model):
    """Таблица с данными для поиска"""
    url_groupe = models.URLField(primary_key=True, blank=True, verbose_name="URL Группы")
    search_string = models.CharField(max_length=200, null=False, blank=True, verbose_name="Искомая строка")

    def __str__(self):
        return f'{self.url_groupe}'

    class Meta:
        verbose_name = 'Данные для поиска'
        verbose_name_plural = 'Данные для поиска'


class found_data(models.Model):
    """Таблица с данными для вывода"""
    url_groupe = models.ForeignKey('search_data', on_delete=models.PROTECT, null=True, verbose_name="URL Группы")
    date = models.DateTimeField(null=True, blank=False, auto_now_add=False, verbose_name="Дата и время")
    found_text = models.TextField(null=True, verbose_name='Найденные данные')

    def __str__(self):
        return f'{self.url_groupe}'

    class Meta:
        verbose_name = 'Результат поиска'
        verbose_name_plural = 'Результаты поиска'

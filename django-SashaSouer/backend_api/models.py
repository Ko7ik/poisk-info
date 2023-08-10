from django.db import models


class search_data(models.Model):
    url_groupe = models.URLField(primary_key=True, blank=True, verbose_name="URL Группы")
    search_text = models.CharField(max_length=200, blank=True, verbose_name="Вводимые данные")

    def __str__(self):
        return self.url_groupe

class found_data(models.Model):
    url_groupe = models.ForeignKey('search_data', on_delete=models.PROTECT, blank=True, verbose_name="URL Группы")
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время")
    found_text = models.TextField(blank=True, verbose_name="Результат")

    def __str__(self):
        return self.found_text


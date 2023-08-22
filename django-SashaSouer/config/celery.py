# -*- coding: utf-8 -*-
import os
from celery import Celery

# Установите переменную окружения 'DJANGO_SETTINGS_MODULE' для настройки Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('your_project')

# Загрузите настройки Django для Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически найдите и зарегистрируйте все задачи (tasks) в приложениях Django
app.autodiscover_tasks()

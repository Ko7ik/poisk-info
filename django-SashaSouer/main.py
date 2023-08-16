# -*- coding: utf-8 -*-
import datetime
import subprocess

import psycopg2
from psycopg2 import sql
import json
import webbrowser

# Запуск сервера Django в отдельном процессе
server_process = subprocess.Popen(['python', 'manage.py', 'runserver', '192.168.0.17:8000'])

# Ваш скрипт
your_script_path = 'parser/main.py'
subprocess.call(['python', your_script_path])

# Подключение к базе данных
conn = psycopg2.connect(
    dbname='proba',
    user='postgres',
    password='12345678',
    host='localhost',  # Укажите хост
    port='5432'  # Укажите порт
)
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
print(data)

try:

    datas = datetime.date.today()
    k = 0
    id = 1
    # Создание курсора
    cursor = conn.cursor()
    # Составление SQL-запроса
    insert_query = sql.SQL("""
        INSERT INTO public.backend_api_founddata (id,id_post, img, found_text)
        VALUES (%s,%s,%s, %s)
    """)

    while k < len(data):
        # Выполнение запроса
        cursor.execute(insert_query, (
            id,
            data[k]['id'],
            data[k]['image'],
            data[k]['text']
        ))
        k += 1
        id += 1
        # Фиксация изменений
        conn.commit()

except Exception as e:
    print("Ошибка:", e)
    conn.rollback()

finally:
    # Закрытие соединения
    conn.close()
# Остановка сервера Django после выполнения скрипта
server_process.terminate()

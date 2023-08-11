# Generated by Django 4.2.4 on 2023-08-10 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='search_data',
            fields=[
                ('url_groupe', models.URLField(blank=True, primary_key=True, serialize=False, verbose_name='URL Группы')),
                ('search_text', models.CharField(blank=True, max_length=200, verbose_name='Вводимые данные')),
            ],
        ),
        migrations.CreateModel(
            name='found_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('found_text', models.TextField(blank=True, verbose_name='Результат')),
                ('url_groupe', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='backend_api.search_data', verbose_name='URL Группы')),
            ],
        ),
    ]
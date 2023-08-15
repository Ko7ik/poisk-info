# Generated by Django 4.2.4 on 2023-08-10 08:59

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
                ('search_string', models.CharField(blank=True, max_length=200, verbose_name='Искомая строка')),
            ],
            options={
                'verbose_name': 'Данные для поиска',
                'verbose_name_plural': 'Данные для поиска',
            },
        ),
        migrations.CreateModel(
            name='found_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата и время')),
                ('found_text', models.TextField(null=True, verbose_name='Найденные данные')),
                ('url_groupe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend_api.search_data', verbose_name='URL Группы')),
            ],
            options={
                'verbose_name': 'Результат поиска',
                'verbose_name_plural': 'Результаты поиска',
            },
        ),
    ]

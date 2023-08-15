# Generated by Django 4.2.4 on 2023-08-14 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_group', models.URLField(blank=True, verbose_name='URL Группы')),
                ('search_string', models.CharField(blank=True, max_length=200, verbose_name='Искомая строка')),
            ],
            options={
                'verbose_name': 'Данные для поиска',
                'verbose_name_plural': 'Данные для поиска',
            },
        ),
        migrations.CreateModel(
            name='FoundData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(blank=True, max_length=50, verbose_name='Дата и время публикации')),
                ('image', models.FileField(upload_to='img/', verbose_name='Изображения')),
                ('text', models.TextField(null=True, verbose_name='Найденные данные')),
                ('id_post', models.CharField(blank=True, max_length=20, verbose_name='ID поста')),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='backend_api.searchdata', verbose_name='URL Группы')),
            ],
            options={
                'verbose_name': 'Результат поиска',
                'verbose_name_plural': 'Результаты поиска',
            },
        ),
    ]

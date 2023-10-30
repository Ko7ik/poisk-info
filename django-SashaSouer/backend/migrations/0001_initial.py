# Generated by Django 4.2.5 on 2023-09-26 07:02

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id_social', models.AutoField(db_column='id_social', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', verbose_name='Название соцсети')),
            ],
            options={
                'db_table': 'social_network',
            },
        ),
        migrations.CreateModel(
            name='StatusTask',
            fields=[
                ('id_status', models.AutoField(db_column='id_status', primary_key=True, serialize=False)),
                ('status', models.CharField(db_column='status', verbose_name='Статус таска')),
            ],
            options={
                'db_table': 'status_task',
            },
        ),
        migrations.CreateModel(
            name='VkParserData',
            fields=[
                ('id_data', models.AutoField(db_column='id_data', primary_key=True, serialize=False)),
                ('login', models.CharField(db_column='login', verbose_name='Логин')),
                ('password', models.CharField(db_column='password', verbose_name='Пароль')),
            ],
            options={
                'db_table': 'vk_parser_data',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user_identifier', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id_task_name', models.AutoField(db_column='id_task_name', primary_key=True, serialize=False)),
                ('search_text', models.CharField(db_column='search_text', verbose_name='Искомый текст')),
                ('date', models.DateTimeField(auto_now_add=True, db_column='date', verbose_name='Дата создания')),
                ('url_source', models.URLField(db_column='url_source', verbose_name='URL цели')),
                ('id_last_post', models.CharField(db_column='id_last_post', default='0', verbose_name='id последнего поста')),
                ('social_net', models.ForeignKey(db_column='social_net', on_delete=django.db.models.deletion.CASCADE, to='backend.socialnetwork', verbose_name='Социальная сеть')),
                ('status', models.ForeignKey(db_column='status', default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.statustask', verbose_name='Статус таска')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('vk_parser_data_id', models.ForeignKey(db_column='vk_parser_data_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.vkparserdata', verbose_name='Данные для парсера')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='FoundData',
            fields=[
                ('id_found_data', models.AutoField(db_column='id_found_data', primary_key=True, serialize=False)),
                ('name_source', models.CharField(blank=True, db_column='name_source', null=True, verbose_name='Цель поиска')),
                ('id_post', models.CharField(db_column='id_post', verbose_name='ID поста')),
                ('date_post', models.CharField(db_column='date_post', verbose_name='Дата публикации')),
                ('img', models.JSONField(blank=True, db_column='img', null=True, verbose_name='Фотография')),
                ('video', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(verbose_name='Видео'), blank=True, db_column='video', null=True, size=None)),
                ('found_text', models.TextField(db_column='found_text', verbose_name='Найденный текст')),
                ('link', models.CharField(db_column='link', verbose_name='Ссылка на публикацию')),
                ('id_task', models.ForeignKey(db_column='id_task', on_delete=django.db.models.deletion.CASCADE, to='backend.task', verbose_name='Таск')),
            ],
            options={
                'db_table': 'found_data',
            },
        ),
    ]
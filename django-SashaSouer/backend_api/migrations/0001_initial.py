# Generated by Django 4.2.4 on 2023-08-28 11:56

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название соцсети')),
            ],
        ),
        migrations.CreateModel(
            name='StatusTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(verbose_name='Статус таска')),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('token_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.token')),
                ('user_identifier', models.IntegerField()),
            ],
            bases=('authtoken.token',),
        ),
        migrations.CreateModel(
            name='VkParserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(verbose_name='Логин')),
                ('password', models.CharField(verbose_name='Пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', models.CharField(verbose_name='Искомый текст')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('url_group', models.URLField(verbose_name='URL Группы')),
                ('id_last_post', models.CharField(default='1991591211346', verbose_name='id последнего поста')),
                ('social_net', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_api.socialnetwork', verbose_name='Социальная сеть')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend_api.statustask', verbose_name='Статус таска')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vk_parser_data_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend_api.vkparserdata', verbose_name='Данные для парсера')),
            ],
        ),
        migrations.CreateModel(
            name='FoundData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_post', models.CharField(verbose_name='ID поста')),
                ('date_post', models.CharField(verbose_name='Дата публикации')),
                ('img', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(verbose_name='Фотография'), blank=True, null=True, size=None)),
                ('found_text', models.TextField(verbose_name='Найденный текст')),
                ('link', models.CharField(verbose_name='Ссылка на публикацию')),
                ('id_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_api.task', verbose_name='Таск')),
            ],
        ),
    ]

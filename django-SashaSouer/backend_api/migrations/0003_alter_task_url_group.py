# Generated by Django 4.2.4 on 2023-08-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_task_id_last_post_alter_founddata_date_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='url_group',
            field=models.CharField(verbose_name='URL Группы'),
        ),
    ]

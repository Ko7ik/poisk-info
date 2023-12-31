# Generated by Django 4.2.5 on 2023-10-11 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertoken',
            options={},
        ),
        migrations.RemoveField(
            model_name='usertoken',
            name='created',
        ),
        migrations.RemoveField(
            model_name='usertoken',
            name='key',
        ),
        migrations.RemoveField(
            model_name='usertoken',
            name='user',
        ),
        migrations.AddField(
            model_name='usertoken',
            name='token_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authtoken.token'),
            preserve_default=False,
        ),
    ]

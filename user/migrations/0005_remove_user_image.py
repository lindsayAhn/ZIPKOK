# Generated by Django 3.1.1 on 2020-11-11 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]

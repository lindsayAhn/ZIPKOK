# Generated by Django 3.1.1 on 2020-11-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0020_auto_20201105_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_thumbnail_url',
        ),
    ]

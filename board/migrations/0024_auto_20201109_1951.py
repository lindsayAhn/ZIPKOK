# Generated by Django 3.1.1 on 2020-11-09 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0023_auto_20201108_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_textfield',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_user',
            new_name='user',
        ),
    ]

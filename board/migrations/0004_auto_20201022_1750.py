# Generated by Django 3.1.1 on 2020-10-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_board_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='photo',
        ),
        migrations.AddField(
            model_name='board',
            name='category',
            field=models.CharField(choices=[('운동', '운동'), ('악기', '악기'), ('요리', '요리')], default='', max_length=2),
        ),
    ]

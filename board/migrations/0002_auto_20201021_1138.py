# Generated by Django 3.1.1 on 2020-10-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='depth',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='groupno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='orderno',
            field=models.IntegerField(default=0),
        ),
    ]

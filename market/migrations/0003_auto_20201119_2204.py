# Generated by Django 3.1.1 on 2020-11-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20201117_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='groupno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='market',
            name='orderno',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='market',
            name='category',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
# Generated by Django 3.1.1 on 2020-11-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20201120_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='price',
            field=models.CharField(blank=True, max_length=10000000),
        ),
    ]
# Generated by Django 3.1.1 on 2020-11-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_merge_20201120_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

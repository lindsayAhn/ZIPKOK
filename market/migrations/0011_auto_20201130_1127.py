# Generated by Django 3.1.1 on 2020-11-30 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_auto_20201130_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='image',
            field=models.ImageField(default='frame.png', upload_to='images/'),
        ),
    ]
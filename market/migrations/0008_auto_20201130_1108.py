# Generated by Django 3.1.1 on 2020-11-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_market_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='image',
            field=models.ImageField(blank=True, default='/assets/images/frame.png', null=True, upload_to='images/'),
        ),
    ]
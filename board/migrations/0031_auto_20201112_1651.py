# Generated by Django 3.1.1 on 2020-11-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0030_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/check.png', upload_to=''),
        ),
    ]

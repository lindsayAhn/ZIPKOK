# Generated by Django 3.1.1 on 2020-11-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20201112_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='/profiles/user.png', upload_to='profiles/'),
        ),
    ]
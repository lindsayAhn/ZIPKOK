# Generated by Django 3.1.1 on 2020-10-27 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_auto_20201027_2015'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
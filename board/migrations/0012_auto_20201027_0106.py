# Generated by Django 3.1.1 on 2020-10-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_auto_20201027_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
# Generated by Django 3.1.1 on 2020-11-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0032_auto_20201112_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

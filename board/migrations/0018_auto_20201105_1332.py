# Generated by Django 3.1.1 on 2020-11-05 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_board_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
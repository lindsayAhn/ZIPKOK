# Generated by Django 3.1.3 on 2020-11-07 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_remove_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questType', models.IntegerField(default=0)),
                ('lowaccount', models.IntegerField(default=0)),
                ('urladress', models.CharField(max_length=1000)),
                ('recommendationReason', models.CharField(max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]

from django.conf import settings
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    # photo = models.ImageField(upload_to='profiles/', default='user.png')
    password = models.CharField(max_length=32)
    joindate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User({self.name}, {self.email}, {self.password}, {self.joindate}'

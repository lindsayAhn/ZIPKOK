from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    category = models.CharField(max_length=5, null=True)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)
    groupno = models.IntegerField(default=0)
    orderno = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)


class Photo(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)



class Comment(models.Model):
    blog = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, )
    # comment_thumbnail_url = models.TextField(max_length=300)
    comment_textfield = models.TextField(blank=False)




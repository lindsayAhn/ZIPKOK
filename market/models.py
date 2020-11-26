from django.db import models

# Create your models here.
from django.db.models import DateTimeField, IntegerField

from user.models import User


class Market(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    price = models.CharField(max_length=10000000, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=8, null=True)
    hit = models.IntegerField(default=0)
    regdate: DateTimeField = models.DateTimeField(auto_now=True)
    groupno: IntegerField = models.IntegerField(default=0)
    orderno: IntegerField = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)


class Photo(models.Model):
    post = models.ForeignKey(Market, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class Comment(models.Model):
    blog = models.ForeignKey(Market, on_delete=models.CASCADE, null=True, related_name='market_comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='market_comments')
    # comment_thumbnail_url = models.TextField(max_length=300)
    comment_textfield = models.TextField(blank=False)




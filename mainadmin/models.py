from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminPost(models.Model):
    date_created = models.DateField(auto_now_add=True)
    post_name = models.CharField(max_length=100)

class ImagePosts(models.Model):
    image_add = models.ForeignKey(AdminPost,related_name='adminposts',on_delete=models.CASCADE)
    images = models.ImageField()
    description = models.CharField(max_length=150)
    tag = models.CharField(max_length=10)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

class StatusTable(models.Model):
    date_of_change = models.DateField(auto_now_add=True)
    posts = models.ForeignKey(ImagePosts,related_name='imagepost',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status_from_user = models.CharField(default="Unlike",max_length=30)
    action = models.BooleanField(default=True)
    



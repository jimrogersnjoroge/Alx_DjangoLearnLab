from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from taggit.managers import TaggableManager

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.URLField(blank=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content   
    
class Tag(models.Model):
    post = models.ManyToManyField(Post)
    name = models.CharField(max_length=50)  

    tags = TaggableManager()

    def __str__(self):
        return self.name 
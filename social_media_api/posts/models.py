from django.db import models

#Create your models here.
#Post Model
class Post(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

#Comment Model
class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
    
#Implementing Notifications and Likes Functionality
#Like Model
class Like(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.author.username} liked {self.post.title}"


from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    feat_img = CloudinaryField('image', default='placeholder')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts')
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='forumpost_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='forum_posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='postcomment_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']

    def number_of_likes(self):
        return self.likes.count()
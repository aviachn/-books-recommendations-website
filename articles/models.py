from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):     #the class is going to inherit from models.Model, it's inbuild in django, inherit some basic functionality that all models will have
    title = models.CharField(max_length = 100)
    slug = models.SlugField()   #the URL addres of the article
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default ='default.png', blank = True)
    author = models.ForeignKey(User, default=None, on_delete=None)
    quote = models.TextField(default=None)
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:220]+'...'

from django.db import models

# Create your models here.
class Entry(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
    	return self.username

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200,unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Register(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    re_email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    birthday = models.TimeField()

    def __str__(self):
        return self.username
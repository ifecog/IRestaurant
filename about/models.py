from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_link = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    name = models.CharField(max_length=50)
    body = RichTextField()
    
    def __str__(self):
        return self.name
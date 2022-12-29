from django.db import models
from menu.models import Category
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    body = RichTextField()
    upload_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

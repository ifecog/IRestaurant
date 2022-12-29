from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='media/categories/%y/%m/%d/', blank=True)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/meals/%y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    preparation_time = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, unique=True)
    upload_time = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=14)
    date = models.DateField()
    time = models.TimeField()
    no_of_persons = models.IntegerField()
    
    def __str__(self):
        return self.name
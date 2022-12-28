from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/categories/%y/%m/%d/', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    

class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='media/meals/%y/%m/%d/', blank=True)
    persons = models.IntegerField()
    price = models.DecimalField(max_digits=5)
    preparation_time = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return self.name

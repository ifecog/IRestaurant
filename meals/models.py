from django.db import models

# Create your models here.


class Feature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=100)
    image = models.ImageField(upload_to='testimonials/%y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

from email import message
from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    date_sent = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email

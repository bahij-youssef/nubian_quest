from django.db import models
from datetime import datetime


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

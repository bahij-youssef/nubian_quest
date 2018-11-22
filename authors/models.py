from django.db import models
from datetime import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    creation_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

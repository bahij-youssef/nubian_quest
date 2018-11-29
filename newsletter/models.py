from django.db import models
from datetime import datetime


class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    join_date = models.DateTimeField(default=datetime.now)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

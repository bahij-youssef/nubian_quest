from django.db import models
from datetime import datetime
from tinymce.models import HTMLField
from authors.models import Author


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, null=True)
    keywords = models.TextField(blank=True)
    #category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    content = HTMLField()
    headline = models.TextField(null=True)
    is_draft = models.BooleanField(default=False)
    date_published = models.DateTimeField(default=datetime.now)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    audio_mp3 = models.FileField(
        upload_to='audio/%Y/%m/%d/', blank=True, null=True)
    audio_ogg = models.FileField(
        upload_to='audio/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title

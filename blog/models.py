from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)


    class Meta:
        ordering = ['-published']    

    def __str__(self):
        return self.title   

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url     
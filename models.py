from django.db import models
from django.utils import timezone


# Create your models here.

class Film(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, default='film')
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100, default='genre')
    cast = models.CharField(max_length=100, default='cast')
    rating = models.FloatField(blank=True, null=True)
    createDate = models.DateTimeField(blank=True, null=True)
    list_display = ('title', 'year'),


def release(self):
    self.createDate = timezone.now()
    self.save()


def __str__(self):
    return self.title


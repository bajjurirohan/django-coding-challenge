from django.db import models
from .movie import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.IntegerField()
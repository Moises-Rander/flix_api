from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=500)
    rate = models.FloatField(editable=False, null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    actors = models.ManyToManyField(Actor, related_name='actor_movies')
    release_date = models.DateField(null=True, blank=True)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

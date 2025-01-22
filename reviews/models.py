from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='movie_reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'A avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(5, 'A avaliação não pode ser superior a 5 estrelas.'),
        ]
    )
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.title

from django.db.models.signals import post_save
from django.dispatch import receiver
from reviews.models import Review


@receiver(post_save, sender=Review)
def calculate_movie_rate_on_review_save(sender, instance, **kwargs):
    movie = instance.movie
    reviews = movie.movie_reviews.all()
    if reviews.exists():
        movie.rate = sum(review.stars for review in reviews) / reviews.count()
    else:
        movie.rate = 0
    movie.save(update_fields=['rate'])

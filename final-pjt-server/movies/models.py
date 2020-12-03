from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=50)
    popularity = models.FloatField()
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    release_date = models.DateField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rates = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
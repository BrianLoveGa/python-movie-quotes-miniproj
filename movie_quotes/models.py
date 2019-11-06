from django.db import models

# Create your models here.

class Quote(models.Model):
    movie_title = models.CharField(default="movie title", max_length=100)
    movie_release_year = models.CharField(default="year", max_length=10)
    imbd_link = models.CharField(default="imdb link", max_length=200)
    movie_poster = models.CharField(default="link to poster or pic", max_length=200)
    movie_quote = models.TextField(default="quote here")


    def __str__(self):
        return self.movie_title and self.movie_quote


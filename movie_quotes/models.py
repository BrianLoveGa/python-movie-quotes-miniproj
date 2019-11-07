from django.db import models

# Create your models here.

## git add content

class Movie(models.Model):
    movie_title = models.CharField(default="movie title", max_length=100)
    movie_release_year = models.CharField(default="year", max_length=10)
    imbd_link = models.CharField(default="imdb link or url", max_length=200)
    movie_poster = models.CharField(default="link to poster or pic", max_length=200)
    def __str__(self):
        return self.movie_title

Movie.objects.order_by('movie_title')


class Quote(models.Model):
    title = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='quotes')
    movie_quote = models.TextField(default="quote here")


    def __str__(self):
        return self.movie_quote

Quote.objects.order_by('title')
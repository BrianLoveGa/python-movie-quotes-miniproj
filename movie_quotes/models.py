from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

## git add content

class Movie(models.Model):
    movie_title = models.CharField(default="movie title", max_length=100, unique=True)
    movie_release_year = models.IntegerField(
                default=1980)
    #             ,
    #     validators=[
    #         MaxValueValidator(2050),
    #         MinValueValidator(1900)
    #     ])
    #  this works to limit the year entry but when implemented and and a year
    #   higher than 2050 or lower than 1900 is entered it crashes the app 
    #    instead of issuing a warning message or pop-up will research more later



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
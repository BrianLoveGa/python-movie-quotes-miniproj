from django import forms
from .models import Movie, Quote


class MovieForm(forms.ModelForm):
    class Meta:

        model = Movie
        fields = (
            "movie_title",
            "movie_release_year",
            "imbd_link",
            "movie_poster",
        )



class QuoteForm(forms.ModelForm):
    class Meta:

        model = Quote
        fields = (
            "title",
            "movie_quote",
        )


from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:

        model = Quote
        fields = (
            "movie_title",
            "movie_release_year",
            "imbd_link",
            "movie_poster",
            "movie_quote",
        )


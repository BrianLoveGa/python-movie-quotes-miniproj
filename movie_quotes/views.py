from django.shortcuts import render, redirect
from .models import Quote, Movie
from .forms import QuoteForm, MovieForm

# Create your views here.

def home(request):
    return render(request, "quotes/home.html",)

# basic list view
# https://stackoverflow.com/questions/5250276/how-to-render-an-ordered-dictionary-in-django-templates
# {"movies": sorted(movies.movie_title())} )


def quote_list(request):
    quotes = Quote.objects.all()
    # movies = Movie.objects.all() ...   ####   {"movies": movies},
    return render(request, "quotes/quote_list.html", {"quotes": quotes} )


def movie_list(request):
    movies = Movie.objects.all()
    #quotes = Quote.objects.all() ... and ####  {"quotes": quotes}
    return render(request, "movies/movie_list.html", {"movies": movies} )


# detail view of an item


def quote_detail(request, pk):
    quote = Quote.objects.get(id=pk)
    
    return render(request, "quotes/quote_detail.html", {"quote": quote})


def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    
    return render(request, "movies/movie_detail.html", {"movie": movie})


# make new ones


def quote_create(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            return redirect("quote_detail", pk=quote.pk)
    else:
        form = QuoteForm()
    return render(request, "quotes/quote_form.html", {"form": form})


def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect("movie_detail", pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, "movies/movie_form.html", {"form": form})


# edit the  data


def quote_edit(request, pk):
    quote = Quote.objects.get(pk=pk)
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid:
            quote = form.save()
            return redirect("quote_detail", pk=quote.pk)
    else:
        form = QuoteForm(instance=quote)
        return render(request, "quotes/quote_form.html", {"form": form})


def movie_edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid:
            movie = form.save()
            return redirect("movie_detail", pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
        return render(request, "movies/movie_form.html", {"form": form})


# delete it


def quote_delete(request, pk):
    Quote.objects.get(id=pk).delete()
    return redirect("quote_list")


def movie_delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect("movie_list")


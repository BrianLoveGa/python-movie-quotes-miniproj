from django.shortcuts import render
from .models import Quote
from .forms import QuoteForm
# Create your views here.

# basic list view 

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes':quotes})


# detail view of an item

def quote_detail(request, pk):
    quote = Quote.objects.get(id=pk)
    return render(request, 'quotes/quote_detail.html', {'quote':quote})


# make new ones

def quote_create(request):
        if request.method == 'POST':
            form = QuoteForm(request.POST)
            if form.is_valid():
                quote = form.save()
                return redirect('quote_detail', pk=quote.pk)
        else:
             form = QuoteForm()
        return render(request, 'quotes/quote_form.html', {'form':form})


# edit the  data 

def quote_edit(request, pk):
    quote = Quote.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid:
            quote = form.save()
            return redirect('quote_detail', pk=quote.pk)
    else:
        form = QuoteForm(instance=quote)
        return render(request, 'quotes/quote_form.html', {'form':form})


# delete it

def quote_delete(request, pk):
    Quote.objects.get(id=pk).delete()
    return redirect('quote_list')
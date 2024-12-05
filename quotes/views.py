from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

from .utils import get_mongo_db
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page=per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author(request, id_):
    author_view = Author.objects.get(id=id_)
    return render(request, 'quotes/author.html', context={'author': author_view})


@login_required
def add_quote(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Нова цитата успішно створена")
            return redirect(to="quotes:add-quote")
    return render(request, 'quotes/add_quote.html', context={"form": form})


@login_required
def add_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Новий автор успішно створений")
            return redirect(to="quotes:add-author")
    return render(request, 'quotes/add_author.html', context={"form": form})

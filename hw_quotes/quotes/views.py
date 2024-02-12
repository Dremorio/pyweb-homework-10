from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Author, Quote, Tag
from .utils import get_mongodb
from django.core.paginator import Paginator


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_on_page})


class AuthorView(DetailView):
    model = Author
    template_name = 'quotes/about_author.html'
    context_object_name = 'author'
    slug_field = 'fullname'
    slug_url_kwarg = 'author'


class QuotesByTagView(DetailView):
    model = Tag
    template_name = 'quotes/tag_detail.html'
    context_object_name = 'tag'
    slug_field = 'name'
    slug_url_kwarg = 'quote'
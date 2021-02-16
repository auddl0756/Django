from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from . models import Book,Author,Publisher

# template view
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] =['Book','Author','Publisher']
        return context


#list view
class BookList(ListView):
    model = Book

class AuthorList(ListView):
    model=Author

class PublisherList(ListView):
    model = Publisher


# detail view

class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher


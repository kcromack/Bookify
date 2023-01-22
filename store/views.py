from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

from .models import Genre, Book

def book_all(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})

def genre_list(request, genre_slug=None):
    genre = get_object_or_404(Genre, slug=genre_slug)
    books = Book.objects.filter(genre=genre)
    return render(request, 'store/books/genre.html', {'genre': genre, 'books': books})

def genres(request):
    return {
        'genres': Genre.objects.all()
    }

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    return render(request, 'store/books/detail.html', {'book': book})





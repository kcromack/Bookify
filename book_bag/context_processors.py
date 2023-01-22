from .book_bag import Book_Bag


def book_bag(request):
    return {'book_bag': Book_Bag(request)}
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from store.models import Book
from .book_bag import Book_Bag

def book_bag_summary(request):
    book_bag = Book_Bag(request)
    return render(request, 'book_bag/summary.html', {'book_bag': book_bag})

def book_bag_add(request):
    book_bag = Book_Bag(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_qty = int(request.POST.get('bookqty'))
        book = get_object_or_404(Book, id=book_id)
        book_bag.add(book=book, qty=book_qty)

        book_bag_qty = book_bag.__len__()
        response = JsonResponse({'qty': book_bag_qty})
        return response
    
def book_bag_delete(request):
    book_bag = Book_Bag(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_bag.delete(book=book_id)

        book_bag_qty = book_bag.__len__()
        book_bag_total = book_bag.get_total_price()
        response = JsonResponse({ 'qty': book_bag_qty, 'subtotal': book_bag_total})
        return response
 
        book_bag_qty = book_bag.__len__()
        book_bag_total = book_bag.get_total_price()
        response = JsonResponse({'qty': book_bag_qty, 'subtotal': book_bag_total})
        return response
    
def book_bag_update(request):
    book_bag = Book_Bag(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_qty = int(request.POST.get('bookqty'))
        book_bag.update(book=book_id, qty=book_qty)

        book_bag_qty = book_bag.__len__()
        book_bag_total = book_bag.get_total_price()
        response = JsonResponse({'qty': book_bag_qty, 'subtotal': book_bag_total})
        return response
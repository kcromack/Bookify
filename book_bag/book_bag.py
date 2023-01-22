from decimal import Decimal
from django.conf import settings
from store.models import Book


class Book_Bag():
    """
    A base Book_Bag class, providing some default behaviors that can be inherited or overided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        book_bag = self.session.get(settings.BOOK_BAG_SESSION_ID)
        if settings.BOOK_BAG_SESSION_ID not in request.session:
            book_bag = self.session[settings.BOOK_BAG_SESSION_ID] = {}
        self.book_bag = book_bag
    
    def add(self, book, qty):
        book_id = str(book.id)

        if book_id in self.book_bag:
            self.book_bag[book_id]['qty'] = qty
        else:
            self.book_bag[book_id] = {'price': str(book.price), 'qty': qty}
            
        self.save()
    
    def __iter__(self):
        book_ids = self.book_bag.keys()
        books = Book.books.filter(id__in=book_ids)
        book_bag = self.book_bag.copy()

        for book in books:
            book_bag[str(book.id)]['book'] = book
        
        for item in book_bag.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the book_bag data and count the qty of items
        """
        return sum(item['qty'] for item in self.book_bag.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.book_bag.values())
    
    def delete(self, book):
        """
        Delete item from session data
        """
        book_id = str(book)
        if book_id in self.book_bag:
            del self.book_bag[book_id]
            self.save()

    def update(self, book, qty):
        """
        Update values in session data
        """
        book_id = str(book)

        if book_id in self.book_bag:
            self.book_bag[book_id]['qty'] = qty
        self.save()
        
    def save(self):
        self.session.modified = True

    def clear(self):
        
        del self.session[settings.BOOK_BAG_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
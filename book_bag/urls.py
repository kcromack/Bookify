from django.urls import path, include
import stripe

from . import views

app_name = 'book_bag'

urlpatterns = [
    path('', views.book_bag_summary, name='book_bag_summary'),
    path('add/', views.book_bag_add, name='book_bag_add'),
    path('delete/', views.book_bag_delete, name='book_bag_delete'),
    path('update/', views.book_bag_update, name='book_bag_update'),
    path('payment/', include('payment.urls', namespace='payment')),
]
from django.urls import path
from . import views
import stripe

app_name = 'payment'

urlpatterns = [
    path('', views.Book_BagView, name='book_bag'),
    path('orderplaced/', views.order_placed, name='order_placed'),
    path('error/', views.Error.as_view(), name='error'),
    path('webhook/', views.stripe_webhook),
]
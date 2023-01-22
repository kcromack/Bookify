from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.book_all, name='book_all'),
    path('bk/<slug:slug>/', views.book_detail, name='book_detail'),
    path('search/<slug:genre_slug>/', views.genre_list, name='genre_list'),
]
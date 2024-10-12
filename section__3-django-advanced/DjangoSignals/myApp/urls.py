from django.urls import path
from .views import save_book, get_all_books_data, delete_books_by_name

urlpatterns =[
 path('books/', save_book, name='myApp-save-books'),
 path('book-list/', get_all_books_data, name='myApp__list-all-books'),
 path('delete-books/<str:name>/', delete_books_by_name, name='myApp__delete-books-by-name')
]
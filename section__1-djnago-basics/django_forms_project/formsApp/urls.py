from django.urls import path
from .views import contact_view, person_view, manage_authors, manage_books

urlpatterns = [
 path("", contact_view, name="home-page"),
 path('person/', person_view, name="formsApp__person-view"),
 path('authors/', manage_authors, name='formsApp__authors-views'),
 path('book-and-authors/<int:book_id>/', manage_books)
]
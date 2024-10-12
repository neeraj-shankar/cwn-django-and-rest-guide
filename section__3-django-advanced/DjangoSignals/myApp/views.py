from django.shortcuts import render, HttpResponse
from .forms import BookForm
from utils.loggers import setup_logger
from .models import Book

logger = setup_logger(__name__)
# Create your views here.

# Handling form data


def get_all_books_data(request):

    # Checking for the get request
    if request.method == "GET":

        # Retrieve all the books instances from database
        books = Book.objects.all()

        return render(request, "myApp/BooksList.html", {"books": books})


def save_book(request):

    if request.method == "POST":

        # Create a form instance with the POST data
        form = BookForm(request.POST)

        # Check if the form is valid (this will automatically validate the data)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            logger.info(f"Form data saved successfully")
            return HttpResponse(f"FORM DATA SAVED")

    else:
        form = BookForm()

    return render(request, "myApp/book.html", {"form": form})

def delete_books_by_name(request, name):

    # Filter all books using requested name
    logger.info(f"Books to be deleted: {name}")
    books = Book.objects.filter(name__icontains=name)
    logger.info(f"All books matching given name: {books}")
    if len(books) == 0:
        logger.error(f"No books with given name found...")

    books.delete()    
    return HttpResponse("All the requested books deleted")
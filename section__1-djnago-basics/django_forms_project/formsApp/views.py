from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, PersonForm, AuthorForm, AuthorBookFormSet
from .utils import setup_logger
from django.forms import formset_factory
from .models import Book, Author

logger = setup_logger(__name__)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            subject = f"Message from {form.cleaned_data['name']}"
            logger.info(f"Received form data: {subject}")
            message = form.cleaned_data['message']
            # Send email or perform other actions
            return render(request, 'formsApp/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'formsApp/contact.html', {'form': form})

def person_view(request):

    if request.method == 'POST': 
        form = PersonForm(request.POST)
        if form.is_valid():

            logger.info(f"Form Data Validated: {form.cleaned_data}")

            return HttpResponse("The form data received and cleaned.")
        
    else:
        form = PersonForm()

    return render(request, 'formsApp/person.html', {'form': form})


def manage_authors(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=3)

    if request.method == "POST":
        formset = AuthorFormSet(request.POST)
        if formset.is_valid():
            # Process formset data
            for form in formset:
                logger.info(form.cleaned_data)
    else:
        formset = AuthorFormSet()

    return render(request, 'formsApp/manage_authors.html', {'formset': formset})

def manage_books(request, book_id):
    book = Book.objects.get(id=book_id)
   # AuthorFormSet = inlineformset_factory(Book, Author, fields=('name', 'email'), extra=2)

    if request.method == "POST":
        formset = AuthorBookFormSet(request.POST, instance=book)
        if formset.is_valid():
            formset.save()
    else:
        formset = AuthorBookFormSet(instance=book)

    return render(request, 'manage_books.html', {'formset': formset})

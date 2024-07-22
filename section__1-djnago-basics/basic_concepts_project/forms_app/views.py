# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

from utils.logging_utils import setup_logger

# Setup logger for this module
logger = setup_logger('forms_app', 'myapp1.log')


def contact_view(request):
    """
    Handle the contact form submission and rendering.

    This view handles both GET and POST requests. For GET requests, it renders
    an empty contact form. For POST requests, it processes the submitted form
    data, validates it, and performs actions such as saving the data or sending
    an email.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object. If the form is submitted and
        valid, it returns a thank you message. Otherwise, it renders the contact
        form template.
    """
    if request.method == 'POST':
        # If the request method is POST, create a form instance with the submitted data
        form = ContactForm(request.POST)
        if form.is_valid():
            # If the form is valid, process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # You can save the data to the database, send an email, etc.
            logger.info(f"Validated Form Data: {name}, {email}, {message}")
            return HttpResponse('Thank you for your message.')
    else:
        # If the request method is GET, create an empty form instance
        form = ContactForm()
    
    # Render the contact form template with the form instance
    return render(request, 'forms_app/contact.html', {'form': form})

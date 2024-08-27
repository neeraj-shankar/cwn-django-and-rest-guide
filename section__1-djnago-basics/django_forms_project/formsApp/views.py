from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, PersonForm
from .utils import setup_logger


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
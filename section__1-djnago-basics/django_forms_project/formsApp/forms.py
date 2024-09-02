from django import forms
from django.core.validators import MaxValueValidator
import email.utils
from django.forms import inlineformset_factory
from .models import Book, Author

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    # def validate_email(self):

    #     email = self.cleaned_data.get('email')
    #     try:
    #         email.utils.parseaddr(email)
    #         return email
    #     except ValueError as ex:
    #         return f"Not a valid email: {ex}"



class PersonForm(forms.Form):
    
    CHOICES = (
        ('tester', 'Test Engineer'),
        ('dev', 'Developer'),
        ('devops', 'Dev Ops'),
        ('sm', 'Scrum Master')
    )

    name = forms.CharField(max_length=50)
    location = forms.CharField(max_length=50)
    age = forms.IntegerField(validators=[MaxValueValidator(120)])
    profession = forms.ChoiceField(choices=CHOICES, required=True)


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

# inline formset using inlineformset_factory, which works for related models (i.e., models with ForeignKey relationships)
AuthorBookFormSet = inlineformset_factory(Author, Book, fields=('__all__'), extra=1)
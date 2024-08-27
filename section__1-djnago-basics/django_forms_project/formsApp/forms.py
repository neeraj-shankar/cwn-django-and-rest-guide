from django import forms
from django.core.validators import MaxValueValidator
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class PersonForm(forms.Form):

    name = forms.CharField(max_length=50)
    location = forms.CharField(max_length=50)
    age = forms.IntegerField(validators=[MaxValueValidator(120)])
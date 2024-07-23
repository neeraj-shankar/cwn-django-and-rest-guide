from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

"""
`TemplateView` is used for rendering a template. 
--------------------------------------------------------------------------
It's a straightforward way to display a static page or a page where the context is dynamically generated.

"""

class HomePageView(TemplateView):
   
   template_name = 'views_app/home.html'
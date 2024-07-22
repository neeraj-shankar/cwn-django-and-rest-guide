from django.urls import path 
from . views import index, test_reverse_mapping_template

app_name = 'my_url_app' # Set the application namespace

urlpatterns = [
    path('', index, name='url-home'),
    path('reverse-url/', test_reverse_mapping_template, name='reverse-url-map'), 
]

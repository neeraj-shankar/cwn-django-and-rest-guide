from .views import PracticeQueriesView
from django.urls import path

urlpatterns = [
    path('', PracticeQueriesView.as_view(), name='home-view-orm'),
]

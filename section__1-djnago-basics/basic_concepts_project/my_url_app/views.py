from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'my_url_app\index.html', context={
        "name": "Neeraj Shankar"
    })

def test_reverse_mapping_template(request):

    return HttpResponse("Reverse Mapping is working")


# D:\Studyzone\cwn-django-and-rest-guide\section__1-djnago-basics\basic_concepts_project\my_url_app\templates\my_url_app\index.html
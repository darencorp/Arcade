from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'views/index.html')

def template(request):
    return render(request, 'views/django_template.html')

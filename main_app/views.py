from django.shortcuts import render
from .models import Cat

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def cats_list(request):
    return render(request, 'cats/cats_list.html', {
        'cats': Cat.objects.all().order_by('id')
    }) 

def cat_details(request, cat_id):
    return render(request, 'cats/cat_details.html', {
        'cat': Cat.objects.get(id=cat_id)
    })
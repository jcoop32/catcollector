from django.shortcuts import render

# models should be used instead
cats = [
    {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
    {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def cats_list(request):
    return render(request, 'cats/cats_list.html', {
        'cats': cats
    }) 
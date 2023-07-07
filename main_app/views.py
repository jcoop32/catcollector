from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Cat
from .forms import FeedingForm

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
    # instantiate FeedingForm to be rendered in the details.html
    feeding_form = FeedingForm()
    return render(request, 'cats/cat_details.html', {
        'cat': Cat.objects.get(id=cat_id),
        'feeding_form': feeding_form
    })

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

class CatUpdate(UpdateView):
    model = Cat
    # selects specific fields from model
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'

def add_feeding(request, cat_id):
    # creates a ModelForm instance using the data that was  
    # submitted in the form
    form = FeedingForm(request.POST)
    # VALIDATES FORMS
    if form.is_valid():
        # dont save the form to the db unitl it 
        # has a cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('details', cat_id=cat_id)
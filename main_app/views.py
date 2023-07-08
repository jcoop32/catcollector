from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Cat
from .forms import FeedingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

# makes sure user is logged in
@login_required
def cats_list(request):
    catLen = Cat.objects.filter(user=request.user).count()
    return render(request, 'cats/cats_list.html', {
        'cats': Cat.objects.filter(user=request.user).order_by('id'),
        'catLen': catLen,
    })

# explore page
@login_required
def explore_list(request):
    return render(request, 'cats/explore_list.html', {
        'cats': Cat.objects.all(),
    }) 

@login_required
def cat_details(request, cat_id):
    # instantiate FeedingForm to be rendered in the details.html
    feeding_form = FeedingForm()
    return render(request, 'cats/cat_details.html', {
        'cat': Cat.objects.get(id=cat_id),
        'feeding_form': feeding_form
    })


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    # selects specific fields from model
    fields = ['breed', 'description', 'age']


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = '/cats'

@login_required
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


def signup(request):
    error_message = ''
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            # saves user to the db
            user = form.save()
            # login new user automatically
            login(request, user)
            return redirect('cats')
    else:
        error_message = 'Invalid signup. Please Try again'
    # bad POST or GET request, render signup
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })

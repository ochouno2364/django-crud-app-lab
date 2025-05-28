from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sneaker 
from .forms import ReleaseForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin






# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

# class Sneaker:
#     def __init__(self, name, brand, description, year, size):
#         self.name = name
#         self.brand = brand
#         self.description = description
#         self.year = year
#         self.size = size

# sneakers = [
#     Sneaker('Cool Grays', 'Jordan', 'Nice gray basketballs shoe', 1989, 10),
#     Sneaker('Walkman 1s', 'Puma', 'Comfortable running shoes', 2011, 9),
#     Sneaker('Panda 1s', 'Nike', 'Black and white style shoes', 2022, 11),
#     Sneaker('Chuck Taylor','Converse', 'High top basketball shoe', 1992, 12),
#     Sneaker('Hyperbalance 7.2', 'New Balance', 'Comforable, stylish running shoes', 2006, 8),
# ]
@login_required
def sneaker_index(request):
    sneakers = Sneaker.objects.filter(user=request.user)
    return render(request, 'sneakers/sneakerindex.html', {'sneakers': sneakers})

@login_required
def sneaker_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    release_form = ReleaseForm()
    return render(request, 'sneakers/detail.html', {
        'sneaker': sneaker, 'release_form': release_form
        })

class SneakerCreate(LoginRequiredMixin, CreateView):
    model = Sneaker
    fields = ['name', 'brand', 'description', 'year', 'size']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SneakerUpdate(LoginRequiredMixin, UpdateView):
    model = Sneaker
    fields = ['brand', 'description', 'year', 'size']

class SneakerDelete(LoginRequiredMixin, DeleteView):
    model = Sneaker
    success_url = '/sneakers/'

@login_required
def add_release(request, sneaker_id):
    form = ReleaseForm(request.POST)
    if form.is_valid():
       new_release = form.save(commit=False)
       new_release.sneaker_id = sneaker_id
       new_release.save()
    return redirect('sneaker-detail', sneaker_id=sneaker_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sneaker-index')
        else:
            error_message = 'Invalid sign up - try again'
            
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

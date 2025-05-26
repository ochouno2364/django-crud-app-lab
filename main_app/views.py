from django.shortcuts import render
from .models import Sneaker 


# Create your views here.
def home(request):
    return render(request, 'home.html')

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

def sneaker_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'sneakers/sneakerindex.html', {'sneakers': sneakers})
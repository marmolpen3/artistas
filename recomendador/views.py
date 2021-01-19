from django.shortcuts import render
from .populate import populateDatabase

# Create your views here.

def index(request):
    return render(request, 'index.html')

def popularBD(request):
    populateDatabase()
    return render(request, 'populate.html')
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'accueil.html')


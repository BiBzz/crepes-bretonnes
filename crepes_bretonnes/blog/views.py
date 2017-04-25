from django.http import Http404
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def bloghome(request):
	return render(request, 'blog/accueil.html')

def date_actuelle(request):
	return render(request, 'blog/date.html', {'date' : datetime.now()})
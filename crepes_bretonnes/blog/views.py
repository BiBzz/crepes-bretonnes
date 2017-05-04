from django.http import HttpResponse, Http404
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def bloghome(request):
	return render(request, 'blog/accueil.html')

def date_actuelle(request):
	return render(request, 'blog/date.html', {'date' : datetime.now()})

def view_article(request, article_id):
    return HttpResponse("Affichage de l'article {0}".format(article_id))

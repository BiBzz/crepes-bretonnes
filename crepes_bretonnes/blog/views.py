from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Post

# Create your views here.
def bloghome(request):
	return render(request, 'blog/accueil.html')

def date_actuelle(request):
	return render(request, 'blog/date.html', {'date' : datetime.now()})

def view_post(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	return render(request, 'blog/view_post.html', locals())

def list_posts(request, year, month):
    return HttpResponse("Liste des articles de {0}/{1}".format(month, year))

def redirect_list_posts(request, year, month):
	return redirect(list_posts, year=year, month=month)

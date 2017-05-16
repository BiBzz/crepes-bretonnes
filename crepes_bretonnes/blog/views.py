from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Post

# Create your views here.
def blog_home(request):
	posts = Post.objects.all()
	return render(request, 'blog/home.html', locals())

def date(request):
	return render(request, 'blog/date.html', {'date' : datetime.now()})

def view_post(request, id, slug):
	post = get_object_or_404(Post, id=id, slug=slug)
	return render(request, 'blog/view_post.html', locals())

def list_posts(request, year, month):
    return HttpResponse("Liste des articles de {0}/{1}".format(month, year))

def redirect_list_posts(request, year, month):
	return redirect(list_posts, year=year, month=month)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender_mail = form.cleaned_data['sender_mail']
        confirmation = form.cleaned_data['confirmation']
        form_sent = True
    return render(request, 'contact.html', locals())

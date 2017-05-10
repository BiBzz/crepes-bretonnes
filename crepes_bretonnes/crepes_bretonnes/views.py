from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'accueil.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender_mail = form.cleaned_data['sender_mail']
        confirmation = form.cleaned_data['confirmation']
      
        form_sent = True

    return render(request, 'contact.html', locals())

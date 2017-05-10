from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label="Sujet")
    message = forms.CharField(widget=forms.Textarea)
    sender_mail = forms.EmailField(label="Votre email")
    confirmation = forms.BooleanField(help_text="Cochez pour recevoir une confirmation", 
required=False)

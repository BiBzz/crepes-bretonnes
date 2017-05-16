from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label="Sujet")
    message = forms.CharField(widget=forms.Textarea)
    sender_mail = forms.EmailField(label="Votre email")
    confirmation = forms.BooleanField(help_text="Cochez pour recevoir une confirmation", required=False)

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')

        if subject and message:
            if "pizza" in subject and "pizza" in message:
                msg = "Merci de ne pas parler de pizza dans le sujet et le message!"
                self.add_error("message", msg)

        return cleaned_data

class NewContactForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    picture = form.ImageField()


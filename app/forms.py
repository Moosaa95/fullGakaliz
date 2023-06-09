from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=200)
    subject = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)




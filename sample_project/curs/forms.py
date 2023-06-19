from django import forms

class ContactForm(forms.Form):
    nume = forms.CharField(required=True)
    email = forms.EmailField()
    mesaj = forms.CharField(widget=forms.Textarea)
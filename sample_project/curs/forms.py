from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    nume = forms.CharField(required=True)
    email = forms.EmailField()
    mesaj = forms.CharField(widget=forms.Textarea)

    def clean_nume(self):
        nume = self.cleaned_data["nume"]
        if nume != nume.title():
            raise ValidationError("Trebuie sa incepea cu litera mare")
        return nume

    def clean(self):
        nume = self.cleaned_data["nume"]
        email = self.cleaned_data["email"]
        if nume not in email:
            raise ValidationError("Numele trebuie sa apara in email")
        return self.cleaned_data
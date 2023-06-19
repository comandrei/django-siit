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

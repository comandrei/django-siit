from django import forms
from django.core.exceptions import ValidationError

from .models import Profesor, Student, Curs

class ContactForm(forms.Form):
    nume = forms.CharField(required=True)
    email = forms.EmailField()
    mesaj = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":10}))

    def clean_nume(self):
        nume = self.cleaned_data["nume"]
        if nume != nume.title():
            raise ValidationError("Trebuie sa incepea cu litera mare")
        return nume

    def clean(self):
        nume = self.cleaned_data.get("nume", "")
        email = self.cleaned_data.get("email", "")
        if nume not in email:
            raise ValidationError("Numele trebuie sa apara in email")
        return self.cleaned_data

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = "__all__"
    #nume = forms.CharField(max_length=10)
    #telefon = forms.CharField(widget=forms.PasswordInput)
    #activ = forms.BooleanField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []
    
    def __init__(self, *args, **kwargs):
        nume_profesor = kwargs.pop("filter_prof")
        super().__init__(*args, **kwargs)
        self.fields["cursuri"].queryset = Curs.objects.filter(profesor__nume=nume_profesor)


        


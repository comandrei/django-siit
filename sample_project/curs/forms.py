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
        if nume_profesor is not None:
            curs_qs = Curs.objects.filter(profesor__nume=nume_profesor)
        else:
            curs_qs = Curs.objects.all()
        self.fields["cursuri"].queryset = curs_qs

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith("@scoalainformala.ro"):
            raise ValidationError("Nu permitem decat email-uri de la scoalainformala.ro")
        return email

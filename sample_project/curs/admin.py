from django.contrib import admin

# Register your models here.
from .models import Curs, Profesor, Student

admin.site.register(Curs)
admin.site.register(Profesor)
admin.site.register(Student)

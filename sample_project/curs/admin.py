from django.contrib import admin

# Register your models here.
from .models import Curs, Profesor

admin.site.register(Curs)
admin.site.register(Profesor)

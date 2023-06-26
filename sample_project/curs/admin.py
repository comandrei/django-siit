from django.contrib import admin

# Register your models here.
from .models import Curs, Profesor, Student

class CursAdmin(admin.ModelAdmin):
    list_display = ("nume", "an", "profesor", "activ")
    list_select_related = ("profesor", )
    list_filter = ("profesor", "activ", "an")
    search_fields = ("nume", "profesor__nume")

admin.site.register(Curs, CursAdmin)
admin.site.register(Profesor)
admin.site.register(Student)

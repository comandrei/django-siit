from django.contrib import admin

# Register your models here.
from .models import Curs, Profesor, Student, Intrebare, Raspuns
from django.db.models import F
from .forms import StudentAdminForm

class CursAdmin(admin.ModelAdmin):
    list_display = ("nume", "an", "profesor", "activ")
    list_select_related = ("profesor", )
    list_filter = ("profesor", "activ", "an")
    search_fields = ("nume", "profesor__nume")

admin.site.register(Curs, CursAdmin)
admin.site.register(Profesor)

def trecere_an(modeladmin, request, queryset):
    queryset.update(an=F('an') + 1)
    # for student in queryset:
    #     student.an = student.an + 1
    #     student.save()
    return

def inca_o_actiune(*args, **kwargs):
    return

class StudentAdmin(admin.ModelAdmin):
    list_display = ("prenume", "nume", "an")
    list_display_links = ("prenume", "nume")
    list_per_page = 3
    change_list_template = "admin/student_change_list.html"
    actions = (trecere_an, inca_o_actiune)
    fieldsets = [
        ("", {"fields": ["nume", "prenume"]}),
        ("Date Contact", {"fields": ["email", "telefon"], "classes": ("collapse", )}),
        ("Cursuri", {"fields": ["cursuri"]})
    ]
    form = StudentAdminForm

admin.site.register(Student, StudentAdmin)
admin.site.register(Intrebare)
admin.site.register(Raspuns)

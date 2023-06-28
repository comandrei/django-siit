"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import re_path, path, include

from curs.views import salut, salut_nume, cursuri, curs, studenti, main, profil, contact, add_profesor, edit_profesor, add_student, login_view
from curs.views import logout_view, api_view, client_app

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path("admin/", admin.site.urls),
    path("salut", salut),
    path("salut/<int:nume>/", salut_nume),
    path("cursuri", cursuri),
    path("curs/<int:curs_id>", curs),
    path("studenti", studenti),
    path("__debug__/", include("debug_toolbar.urls")),
    path("profil", profil),
    path("contact", contact),
    path("adauga_profesor", add_profesor),
    path("adauga_student", add_student),
    path("profesor/<int:profesor_id>/edit", edit_profesor),
    path("login", login_view),
    path("logout", logout_view),
    path("api/", api_view),
    path("client/", client_app),
    path("", main),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns.append(re_path(r"^static/(?P<path>.*)$", views.serve))
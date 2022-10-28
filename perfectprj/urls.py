"""perfectprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from perfectapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path("showregister",views.showregister),
    path("register",views.register),
    path("login/",views.login),
    path("add",views.add),
    path("view/",views.view),
    path("update/",views.update),
    path("delete/",views.delete),
    path("check/",views.check),
    path("mailcheck/",views.mailcheck),
    path("next/",views.next),
    path("previous/",views.previous),
    path("currentans/",views.currentans),
    path("cal/",views.cal),
    path("showtime/",views.showtime)
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

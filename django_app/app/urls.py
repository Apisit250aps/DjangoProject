from django.contrib import admin
from django.urls import path

from . import views as app

urlpatterns = [
    path('', app.home, name='homepage'),
    path('about', app.about, name='about'),
    path('contacts', app.contacts, name='contacts'),
    
]

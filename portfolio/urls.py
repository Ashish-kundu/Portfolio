from django.contrib import admin
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("about",views.about,name='About'),
    path("achievement",views.achievement,name='Achievement'),
    path("project",views.project,name='Poject'),
    path("contact",views.contact,name='Contact')
    
]
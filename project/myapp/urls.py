
from django.contrib import admin
from django.urls import path
from .views import salary,geography,skills,home_page , basez


urlpatterns = [
    path('',home_page,name='home'),
    path('sal/',salary,name='salary'),
    path('skills/',skills,name='skills'),
    path('geo/',geography,name='geography'),
    path('base/',basez,name='base')
]

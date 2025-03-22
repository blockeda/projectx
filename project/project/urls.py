
from django.contrib import admin
from django.urls import path
from ..myapp.views import salary,geography,skills,page


urlpatterns = [
    path('',page,name='page'),
    path('sal/',salary,name='salary'),
    path('skills/',skills,name='skills'),
    path('geo/',geography,name='geography'),
]
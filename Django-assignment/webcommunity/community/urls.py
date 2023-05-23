from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
]

from django.contrib import admin
from django.urls import path
from ajax import views 
urlpatterns = [
    path('', views.home),
    path('json', views.json)
]

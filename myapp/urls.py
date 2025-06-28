from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_say),
    path('home/', views.homepage),
    path('about/', views.about),
    path('contact/', views.contact)  
]
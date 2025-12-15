from django.urls import path
from . import views

urlpatterns = [
    path('allorders/', views.my_orders),
]
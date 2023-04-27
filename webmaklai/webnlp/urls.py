from django.urls import path
from . import views

urlpatterns=[
    path('reph/', views.home, name='reph')

]
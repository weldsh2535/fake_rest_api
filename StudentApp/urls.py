from django.urls import path
from StudentApp import views

urlpatterns =[
    path('student', views.studentApi),
]
from django.urls import path
from StudentApp import views

urlpatterns =[
    path('student/', views.studentApi, name='student-list'),  # Handles GET for all students and POST
    path('student/<int:id>/', views.studentApi, name='student-detail'),  # Handles GET, PUT, DELETE for a single student
]
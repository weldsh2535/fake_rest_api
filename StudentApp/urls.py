from django.urls import path
from StudentApp import views

urlpatterns =[
    path('student', views.get_student, name='student-list'),
    path('student/create',views.create_student,name='create_student'),# Handles GET for all students and POST
    path('student/<int:pk>', views.student_detail, name='student-detail'),  # Handles GET, PUT, DELETE for a single student
]
from django.urls import path
from sms_api import views

urlpatterns =[
    #Student
    path('student', views.get_student, name='student-list'),
    path('student/create',views.create_student,name='create_student'),# Handles GET for all students and POST
    path('student/<int:pk>', views.student_detail, name='student-detail'),  # Handles GET, PUT, DELETE for a single student

   #Course
    path('course', views.get_courses, name="course-list"),
    path('course/create',views.create_course,name='create_course'),
    path('course/<int:pk>', views.course_detail, name='course-detail'),

   #Staff
    path('staff', views.get_staff, name='staff-list'),
    path('staff/create',views.add_staff,name='create_staff'),
    path('staff/<int:pk>', views.staff_detail, name='staff-detail'),

    #Subjects
    path('subject', views.get_subjects, name='subject-list'),
    path('subject/create',views.create_subjects,name='create_subjects'),
    path('subject/<int:pk>', views.subject_detail, name='subject-detail'),

    #Attendances
    path('attendance',views.get_attendance, name='attendance-list'),
    path('attendance/create',views.create_attendance, name='create_attendance'),
    path('attendance/<int:pk>',views.attendance_detail, name='attendance-detail'),

    #Staff FeedBack
    path('staff_feedback',views.get_staff_feedback,name='staff-feedback-list'),
    path('staff_feedback/create',views.create_staff_feedback,name='create_staff_feedback'),
    path('staff_feedback/<int:pk>',views.staff_feedback_detail,name='staff-feedback-detail'),

   #Attendance Report
    path('attendance_report',views.get_attendance_report,name='attendance-report'),
    path('attendance_report/create', views.create_attendance_report,name='create_attendance_report'),
    path('attendance_report/<int:pk>', views.attendance_report_detail,name='attendance-report-detail'),
]
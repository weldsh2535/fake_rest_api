from django.contrib import admin
from django.contrib.auth.backends import UserModel

# Register your models here.
from .models import Students, Admin, Courses, Staffs, Subjects, Attendances, AttendanceReport, LeaveReportStudent, \
    LeaveReportStaff, FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff, CustomUser

# class UserModel(UserModel):
#     pass

admin.site.register(Students)
admin.site.register(Admin)
admin.site.register(CustomUser)
admin.site.register(Courses)
admin.site.register(Staffs)
admin.site.register(Subjects)
admin.site.register(Attendances)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaff)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaff)
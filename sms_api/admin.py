from django.contrib import admin
from django.contrib.auth.backends import UserModel

# Register your models here.
from .models import Students, Admin, Courses, Staffs, Subjects, Attendances, AttendanceReport, LeaveReportStudent, \
    LeaveReportStaff, FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff, CustomUser

# class UserModel(UserModel):
#     pass

class StudentAdmin(admin.ModelAdmin):
    list_display = ["user", "get_first_name", "get_last_name", "get_email","get_course", "gender", "address", "profile_picture"]
    fields = ["curse_id","user", "gender", "address", "profile_picture"]

    # Display first_name from the related CustomUser model
    @admin.display(ordering="user__first_name", description="First Name")
    def get_first_name(self, obj):
        return obj.user.first_name

    # Display last_name from the related CustomUser model
    @admin.display(ordering="user__last_name", description="Last Name")
    def get_last_name(self, obj):
        return obj.user.last_name

    # Display email from the related CustomUser model
    @admin.display(ordering="user__email", description="Email")
    def get_email(self, obj):
        return obj.user.email
    @admin.display(ordering="curse_id", description="Course Name")
    def get_course(self, obj):
        return obj.curse_id.course_name if obj.curse_id else ""

admin.site.register(Students,StudentAdmin)
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
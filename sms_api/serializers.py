from rest_framework import serializers
from sms_api.models import Students, Courses, Staffs, CustomUser, Subjects, Attendances, AttendanceReport, \
    LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'  # Corrected the typo here
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendances
        fields = '__all__'
class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = '__all__'

class LeaveReportStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStudent
        fields = '__all__'
class LeaveReportStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStaff
        fields = '__all__'
class FeedBackStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackStudent
        fields = '__all__'
class FeedBackStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackStaff
        fields = '__all__'
class NotificationStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStudent
        fields = '__all__'
class NotificationStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStaff
        fields = '__all__'
from urllib import request

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from sms_api.models import Students, Courses, Staffs, Subjects, Attendances, FeedBackStaff, AttendanceReport, CustomUser
from sms_api.serializers import StudentSerializer, CourseSerializer, StaffSerializer, CustomUserSerializer, \
    SubjectSerializer, AttendanceSerializer, FeedBackStaffSerializer, AttendanceReportSerializer


@api_view(['GET'])
def get_student(request):
     students = Students.objects.all()
     student_serializer = StudentSerializer(students, many=True)
     return Response(student_serializer.data)
 
@api_view(['POST'])
def create_student(request):
    # Creating the user data
    user_data = {
        "username": request.data.get("username"),
        "password": request.data.get("password"),
        "email": request.data.get("email"),
        "first_name": request.data.get("first_name"),
        "last_name": request.data.get("last_name"),
        "user_type": 3,  # 3 indicates Student
    }

    user_serializer = CustomUserSerializer(data=user_data)
    # print(user_serializer)
    if user_serializer.is_valid():
        user = user_serializer.save()  # Save the CustomUser instance

        curse_id = request.data.get("curse_id")
        address = request.data.get("address")
        profile_picture = request.data.get("profile_picture")
        gender = request.data.get("gender")

        print("Course Id is", curse_id)

        # Ensure that 'curse_id' is provided and not null
        if not curse_id:
            return Response({"error": "curse_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the student instance
        student = Students.objects.create(
            user=user,
            curse_id_id=curse_id,
            address=address,
            profile_picture=profile_picture,
            gender=gender
        )

        # Prepare the response data
        student_data = {
            "user": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "address": student.address,
            "email": user.email,
            "curse_id": student.curse_id_id,
        }

        return Response(student_data, status=status.HTTP_201_CREATED)

    else:
        # Return errors from the CustomUserSerializer
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def student_detail(request,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        try:
            student = Students.objects.get(id=pk)
            student_serializer = StudentSerializer(student)
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        except Students.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        student_data = request.data
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student = Students.objects.get(StudentId=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Courses
@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    course_serializer = CourseSerializer(courses, many=True)
    return  Response(course_serializer.data)
@api_view(['POST'])
def create_course(request):
    course_data = request.data
    course_serializer = CourseSerializer(data=course_data)
    if course_serializer.is_valid():
        course_serializer.save()
        return Response(course_serializer.data, status=status.HTTP_201_CREATED)
    return Response(course_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def course_detail(request,pk):
    try:
        course = Courses.objects.get(pk=pk)
    except Courses.DoesNotExist:
        return Response({"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            course = Courses.objects.get(id=pk)
            course_serializer = CourseSerializer(course)
            return Response(course_serializer.data, status=status.HTTP_200_OK)
        except Courses.DoesNotExist:
            return Response({"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        course_data = request.data
        course_serializer = CourseSerializer(course, data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data)
        return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course = Courses.objects.get(id=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Staff
@api_view(['GET'])
def get_staff(request):
    staff = Staffs.objects.all()
    staff_serializer = StaffSerializer(staff, many=True)
    return Response(staff_serializer.data)

@api_view(['POST'])
def create_staff(request):
    staff_data = request.data
    staff_serializer = StaffSerializer(data=staff_data)
    if staff_serializer.is_valid():
        staff_serializer.save()
        return Response(staff_serializer.data, status=status.HTTP_201_CREATED)

    return Response(staff_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def staff_detail(request,pk):
    try:
        staff = Staffs.objects.get(pk=pk)
    except Staffs.DoesNotExist:
        return Response({"message": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            staff = Staffs.objects.get(pk=pk)
            staff_serializer = StaffSerializer(staff)
            return Response(staff_serializer.data, status=status.HTTP_200_OK)
        except Staffs.DoesNotExist:
            return Response({"message": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        staff_data = request.data
        staff_serializer = StaffSerializer(staff_data, data=staff_data)
        if staff_serializer.is_valid():
            staff_serializer.save()
            return Response(staff_serializer.data)
        return Response(staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        staff = Staffs.objects.get(pk=pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Subjects
@api_view(['GET'])
def get_subjects(request):
    try:
        subjects = Subjects.objects.all()
        subject_serializer = SubjectSerializer(subjects, many=True)
        return Response(subject_serializer.data)
    except Subjects.DoesNotExist:
        return Response({"message": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_subjects(request):
    subject_data = request.data
    subject_serializer = SubjectSerializer(data=subject_data)
    if subject_serializer.is_valid():
        subject_serializer.save()
        return Response(subject_serializer.data, status=status.HTTP_201_CREATED)

    return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def subject_detail(request,pk):
    try:
        subject = Subjects.objects.get(pk=pk)
    except Subjects.DoesNotExist:
        return Response({"message": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        try:
            subject = Subjects.objects.get(pk=pk)
            subject_serializer = SubjectSerializer(subject)
            return Response(subject_serializer.data, status=status.HTTP_200_OK)

        except Subjects.DoesNotExist:
            return Response({"message": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        subject_data = request.data
        subject_serializer = SubjectSerializer(subject, data=subject_data)
        if subject_serializer.is_valid():
            subject_serializer.save()
            return Response(subject_serializer.data)
        return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subject = Subjects.objects.get(pk=pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Attendances
@api_view(['GET'])
def get_attendance(request):
    try:
        attendance = Attendances.objects.all()
        attendance_serializer = AttendanceSerializer(attendance, many=True)
        return Response(attendance_serializer.data)
    except Attendances.DoesNotExist:
        return Response({"message": "Attendance not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_attendance(request):
    attendance_data = request.data
    attendance_serializer = AttendanceSerializer(data=attendance_data)
    if attendance_serializer.is_valid():
        attendance_serializer.save()
        return Response(attendance_serializer.data, status=status.HTTP_201_CREATED)

    return Response(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def attendance_detail(request,pk):
    try:
        attendance = Attendances.objects.get(pk=pk)
    except Attendances.DoesNotExist:
        return Response({"message": "Attendance not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            attendance = Attendances.objects.get(pk=pk)
            attendance_serializer = AttendanceSerializer(attendance)
            return Response(attendance_serializer.data, status=status.HTTP_200_OK)

        except Attendances.DoesNotExist:
            return Response({"message": "Attendance not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        attendance_data = request.data
        attendance_serializer = AttendanceSerializer(attendance_data, data=attendance_data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response(attendance_serializer.data)

        return Response(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        attendance = Attendances.objects.get(pk=pk)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Staff_feedback
@api_view(['GET'])
def get_staff_feedback(request):
    try:
        staff_feedback = FeedBackStaff.objects.all()
        staff_feedback_serializer = FeedBackStaffSerializer(staff_feedback, many=True)
        return Response(staff_feedback_serializer.data)
    except FeedBackStaff.DoesNotExist:
        return Response({"message": "Staff Feed Back not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_staff_feedback(request):
    staff_feedback_data = request.data
    staff_feedback_serializer = FeedBackStaffSerializer(data=staff_feedback_data)
    if staff_feedback_serializer.is_valid():
        staff_feedback_serializer.save()
        return Response(staff_feedback_serializer.data, status=status.HTTP_201_CREATED)

    return Response(staff_feedback_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def staff_feedback_detail(request,pk):
    try:
        staff_feedback = FeedBackStaff.objects.get(pk=pk)
    except FeedBackStaff.DoesNotExist:
        return Response({ "message": "Staff Feed Back not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            staff_feedback = FeedBackStaff.objects.get(pk=pk)
            staff_feedback_serializer = FeedBackStaffSerializer(staff_feedback)
            return Response(staff_feedback_serializer.data, status=status.HTTP_200_OK)

        except FeedBackStaff.DoesNotExist:
            return Response({ "message": "Staff Feed Back not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        staff_feedback_data = request.data
        staff_feedback_serializer = FeedBackStaffSerializer(staff_feedback_data, data=staff_feedback_data)
        if staff_feedback_serializer.is_valid():
            staff_feedback_serializer.save()
            return Response(staff_feedback_serializer.data)

        return Response(staff_feedback_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        staff_feedback = FeedBackStaff.objects.get(pk=pk)
        staff_feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#AttendanceReport
@api_view(['GET'])
def get_attendance_report(request,pk):
    try:
        attendance_report = AttendanceReport.objects.all()
        attendance_report_serializer = AttendanceReportSerializer(attendance_report)
        return Response(attendance_report_serializer.data)
    except AttendanceReport.DoesNotExist:
        return Response({"message": "Attendance report not found"}, status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def create_attendance_report(request):
    try:
        attendance_report_data = request.data
        attendance_report_serializer = AttendanceReportSerializer(data=attendance_report_data)
        if attendance_report_serializer.is_valid():
            attendance_report_serializer.save()
            return Response(attendance_report_serializer.data)

        return Response(attendance_report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except AttendanceReport.DoesNotExist:
        return Response({"message": "Attendance report not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT','GET','DELETE'])
def attendance_report_detail(request,pk):
    try:
        attendance_report = AttendanceReport.objects.get(pk=pk)
    except AttendanceReport.DoesNotExist:
        return Response({"message": "Attendance report not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            attendance_report_serializer = AttendanceReportSerializer(attendance_report)
            return Response(attendance_report_serializer.data, status=status.HTTP_200_OK)
        except AttendanceReport.DoesNotExist:
            return  Response({"message": "Attendance report not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        attendance_report_data = request.data
        attendance_report_serializer = AttendanceReportSerializer(data=attendance_report_data)
        if attendance_report_serializer.is_valid():
            attendance_report_serializer.save()
            return Response(attendance_report_serializer.data)

        return Response(attendance_report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        attendance_report = AttendanceReport.objects.get(pk=pk)
        attendance_report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_staff(request):
    # Creating the user data
    user_data = {
        "username": request.data.get("username"),
        "password": request.data.get("password"),
        "email": request.data.get("email"),
        "first_name": request.data.get("first_name"),
        "last_name": request.data.get("last_name"),
        "user_type": 2,  # 2 indicates Staff
    }
    user_serializer = CustomUserSerializer(data=user_data)
    # print("Error of staff adding user", user_serializer)
    if user_serializer.is_valid():
        user = user_serializer.save()  # Save the CustomUser instance
        # Creating the staff data
        staff_data = {
            "user": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name, # Assign the user ID to the staff data
            "email": user.email,
            "address": request.data.get("address"),
        }
        user.staffs.address = request.data.get("address")
        user.staffs.save()
        return Response(staff_data, status=status.HTTP_201_CREATED)
    else:
        # Return errors from the CustomUserSerializer
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

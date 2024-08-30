from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  # Fix the typo here
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StudentApp.models import Students
from StudentApp.serializers import StudentSerializer

@csrf_exempt
def studentApi(request, id=0):  # Also fixed typo in 'request'
    if request.method == 'GET':
        students = Students.objects.all()
        student_serializer = StudentSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
    
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Add Success", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Students.objects.get(StudentId=student_data['StudentId'])
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Update Success", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method == 'DELETE':
        student = Students.objects.get(StudentId=id)
        student.delete()
        return JsonResponse("Delete Successfully", safe=False)

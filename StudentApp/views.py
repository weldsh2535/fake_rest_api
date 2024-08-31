from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from StudentApp.models import Students
from StudentApp.serializers import StudentSerializer

@api_view(['GET'])
def get_student(request):
     students = Students.objects.all()
     student_serializer = StudentSerializer(students, many=True)
     return Response(student_serializer.data)
 
@api_view(['POST'])
def create_student(resquest):
    student_data = resquest.data
    student_serializer = StudentSerializer(data=student_data)
    if student_serializer.is_valid():
        student_serializer.save()
        return Response(student_serializer.data, status=status.HTTP_201_CREATED)
    return Response(student_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','GET','DELETE'])
def student_detail(request,pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        try:
            student = Students.objects.get(StudentId=pk)
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

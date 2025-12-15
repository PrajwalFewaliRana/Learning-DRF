# from django.http import HttpResponse,JsonResponse
# from django.shortcuts import render
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import  api_view

# Create your views here.
#for api endpoint

@api_view(['GET','POST']) #if we want studentsView only accessable using Get request
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save() #like commit
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def studentDetailView(request,pk):
    try:
        student= Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
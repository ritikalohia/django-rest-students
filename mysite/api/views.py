from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from api import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/students/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of list'
        },
        {
            'Endpoint': '/students/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/students/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new note with data sent in post req'
        },
        {
            'Endpoint': '/students/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing note with data sent in post req'
        },
        {
            'Endpoint': '/students/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes the existing node'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getStudents(request):
    notes = Student.objects.all()
    serializer = StudentSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudent(request, pk):
    note = Student.objects.get(id=pk)
    serializer = StudentSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateStudent(request, pk):
    data = request.data   
    note = Student.objects.get(id=pk)

    serializer = StudentSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteStudent(request, pk):
    note = Student.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted")
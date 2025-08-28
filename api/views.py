from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def all_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)
    

@api_view(['POST'])
def new_todo(request):
    serializer = TodoSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
def edit_todo(request, id):
    try:
        todo = Todo.objects.get(id = id)
        
        if request.method == 'PUT':
            serializer = TodoSerializer(todo, data = request.data, partial = True)

            if serializer.is_valid():
                serializer.save()

                return Response(status=status.HTTP_200_OK)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'GET':
            serializer = TodoSerializer(todo)

            return Response(serializer.data)
         
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def del_todo(request, id):
    try:
        todo = Todo.objects.get(id = id)
        todo.delete()

        return Response(status=status.HTTP_200_OK)
    
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
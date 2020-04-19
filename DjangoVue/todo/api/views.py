from rest_framework import generics
from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework import routers


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'

myrouter = routers.DefaultRouter()
myrouter.register(r'todos',TodoView)
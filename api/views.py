from rest_framework import viewsets
from todo.models import ToDo
from .serializers import ToDoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
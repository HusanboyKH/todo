from django.shortcuts import render, get_object_or_404
from .models import ToDoListModel
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from .serializers import TodoSerializer,StatusSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerPermission


class ListCreateToDoApiView(generics.ListCreateAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)

class RUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwnerPermission,)
class StatusUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoListModel.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsOwnerPermission,)




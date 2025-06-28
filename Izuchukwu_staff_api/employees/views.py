from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EmployeeViewSet():
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET', 'POST']:
            return [IsAuthenticated()]
        return super().get_permissions()  # Default permissions for other methods
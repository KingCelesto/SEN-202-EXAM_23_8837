"""
URL configuration for Izuchukwu_staff_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework.authtoken import views as auth_views
from rest_framework import routers

routers = DefaultRouter()
routers.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(routers.urls)),
    path('api/',include('employees.urls')),
]

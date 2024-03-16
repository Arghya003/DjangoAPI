from django.shortcuts import render
from rest_framework import viewsets
from myapi.models import Company,Employee
from myapi.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
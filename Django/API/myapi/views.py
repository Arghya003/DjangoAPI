from django.shortcuts import render
from rest_framework import viewsets
from myapi.models import Company
from myapi.serializers import CompanySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class  CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    #companies/{companyId}/employees
    

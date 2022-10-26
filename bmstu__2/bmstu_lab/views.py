from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from datetime import date
from bmstu_lab.models import Company, Views_product
from rest_framework import viewsets
from bmstu_lab.serializers import CompanySerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Company.objects.all()
    serializer_class = CompanySerializer  # Сериализатор для модели

def home(request):
    return redirect('company')

def GetCompany(request):
    return render(request, 'company.html', {'data': {
        'current_date': date.today(),
        'com': Company.objects.all()
    }})
def GetProduct(request, id):
    return render(request, 'view_products.html', {'data' : {
        'current_date': date.today(),
        'pro': Views_product.objects.filter(id=id)[0]
    }})
#def GetCompany(request):
 #   com = Company.objects.all()
  #  return(request, 'company.html', { 'com' : com })
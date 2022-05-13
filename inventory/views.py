from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory
# Creafrom django.http import HttpResponse


def index(request):
    return render(request,'index.html')
    return HttpResponse("Hello, world. You're at the polls index.")
def main(request):
    return render(request,'create.html')
def insertv(request):
    return render(request,'index.html')
    a=index(request)
    return HttpResponse(a)
def insert(request):
  if request.method=='POST':
    Name=request.POST['Name']
    Quantity=request.POST['Quantity']
    check=Inventory(Name=Name,Quantity=Quantity)
    check.save()
    
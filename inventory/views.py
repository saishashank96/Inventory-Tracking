from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory,deleted
# Creafrom django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'create.html')
def insertv(request):
    return render(request,'index.html')
    a=index(request)
    return HttpResponse(a)

def insert(request):
 # Inventory.objects.all().delete()
  Name=request.GET['Name']
  if request.method=='GET':
    try:
      if Inventory.objects.get(Name=Name):
          return render(request,'edit2.html')
    except:
      Quantity=request.GET['Quantity']
      check=Inventory(Name=Name,Quantity=Quantity)
      check.save()
    return view(request)
  return HttpResponse('Done')
def view(request):
  objs=Inventory.objects.all()
  return render(request,'display.html',{'obj':objs})
def deletev(request):
  return render(request,'delete.html')
def delete(request):
  Name=request.GET['Name']
  p=Inventory.objects.get(Name=Name) 
  check=deleted(Name=p.Name,Quantity=p.Quantity,Comment=request.GET['Comment'])
  check.save()
  Inventory.objects.get(Name=Name).delete()
  objs=Inventory.objects.all()
  objs1=deleted.objects.all()
  return render(request,'undelete.html',{'obj':objs,'obj1':objs1})
def undelete(request):
  objs1=deleted.objects.all().last()
  #print(objs1)
  check=Inventory(Name=objs1.Name,Quantity=objs1.Quantity)
  check.save()  
  deleted.objects.all().last().delete()
  objs=Inventory.objects.all()
  objs1=deleted.objects.all()  
  return render(request,'display.html',{'obj':objs,'obj1':objs1})
def editv(request):
  return render(request,'edit.html')
def edit(request):
  Name=request.GET['Name']
  Quantity=request.GET['Quantity']
  inv=Inventory.objects.get(Name=Name)
  print(inv)
  inv.Name=Name
  inv.Quantity=Quantity
  inv.save()
  #if request.method == 'GET':
   #     form = Inventory(request.GET, instance=inv)
    #    form.save()
  objs=Inventory.objects.all()
  return render(request,'display.html',{'obj':objs})
    
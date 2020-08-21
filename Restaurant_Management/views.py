from django.http import HttpResponse
from django.shortcuts import render,redirect
from home.models import Restaurent

def base(request):
    return render(request,'base.html')

def add_Restaurant(request):
    return render(request, 'add_Restaurant.html')

def insert_Restaurant(request):
    name= request.POST['name']
    address = request.POST['address']

    addRes = Restaurent(name=name,address=address)
    addRes.save()

    return redirect("/view_Restaurant")


def view_Restaurant(request):
    resList = Restaurent.objects.all()
    return render(request, 'view_Restaurant.html',{'resList':resList})

def edit_Restaurant(request):
    id = request.GET['id']
    getRes = Restaurent.objects.get(pk=id)
    return render(request, 'add_Restaurant.html',{'getRes':getRes})

def update_Restaurant(request):
    id = request.POST['id']
    name = request.POST['name']
    address = request.POST['address']
    updateRes = Restaurent.objects.get(pk=id)
    updateRes.name=name
    updateRes.address=address
    updateRes.save()
    return redirect("/view_Restaurant")

def delete_Restaurant(request):
    id = request.GET['id']
    delRes = Restaurent.objects.get(pk=id)
    delRes.delete()
    return redirect("/view_Restaurant")

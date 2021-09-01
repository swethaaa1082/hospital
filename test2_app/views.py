from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def home(request,c_slug=None):
    c_page=None
    doct=None
    if c_slug!=None:
        c_page=get_object_or_404(Department,slug=c_slug)
        doct=Doctor.objects.filter(department=c_page,available=True)
    else:
        doct=Doctor.objects.all().filter(available=True)
    dpt=Department.objects.all()
    paginator = Paginator(doct,4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        doctors = paginator.page(page)
    except(EmptyPage, InvalidPage):
        doctors = Paginator.page(Paginator.num_pages)

    if request.method=='POST':
        name=request.POST.get('name')
        email= request.POST.get('email')
        department=request.POST.get('department')
        msg= request.POST.get('msg')
        obj=Task(name=name,email=email,department=department,msg=msg)
        obj.save()
        return redirect('/')

    return render(request,"index.html",{'dr':doct,'dp':dpt,'doctors':doctors})
def DoctDetail(request,c_slug,doctor_slug):
    try:
        doctor=Doctor.objects.get(department__slug=c_slug,slug=doctor_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'doctor':doctor})


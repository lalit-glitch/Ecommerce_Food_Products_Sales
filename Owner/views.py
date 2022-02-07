from django.shortcuts import render, redirect
from django.db.models import Q, Count, Avg
from django.contrib import messages
# Create your views here.
from Owner.form import AdminForm
from Customer.models import Feeback_Model, UserRegistration, AdminModel

def adminlogin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            return redirect('uploadpage')
    return render(request,'admin/adminlogin.html')

def uploadpage(request):
    if request.method =="POST":
        forms =AdminForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('uploadpage')
    else:
        forms = AdminForm()
    return render(request,"admin/uploadpage.html",{'v':forms})


def viewfeedback(request):
    obj=Feeback_Model.objects.all()
    return render(request,'admin/viewfeedback.html',{'objects':obj})


def adminlogout(request):
    return redirect('adminlogin')

def updatefood(request):
    obj = AdminModel.objects.all()
    return render(request,'admin/updatefood.html',{'objects':obj})

def customerdetails(request):
    ted = UserRegistration.objects.all()
    return render(request, 'admin/customerdetails.html',{'objects':ted})

def foodchart(request,chart_type):
    chart = Feeback_Model.objects.values('productname').annotate(dcount=Avg('ratings'))
    return render(request,"admin/foodchart.html", {'form':chart, 'chart_type':chart_type})





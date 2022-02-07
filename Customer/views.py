from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Avg, Sum, F
from django.db.models import Q

# Create your views here.
from Customer.models import UserRegistration, Addtocard_Model, Feeback_Model
from Owner.models import AdminModel


def userlogin(request):
    if request.method =="POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            check = UserRegistration.objects.get(firstname=name, password=password)
            request.session['userid'] = check.id
            return  redirect('viewdetails')
        except:
            pass
    return render(request,'user/userlogin.html')

def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobilenumber = request.POST.get('mobilenumber')
        dob= request.POST.get('dob')
        gender= request.POST.get('gender')
        address= request.POST.get('address')
        UserRegistration.objects.create(firstname=firstname, email=email, password=password, mobilenumber=mobilenumber, dob=dob,gender=gender,address=address)
    return render(request, 'user/register.html')


def viewdetails(request):
    obj = AdminModel.objects.all()
    return render(request,'user/viewdetails.html',{'objects':obj})

def viewmodeldetails(request, pk):
    name = request.session['userid']
    userObj = UserRegistration.objects.get(id=name)
    gymObj = AdminModel.objects.get(id=pk)
    amount = gymObj.amount

    if request.method == "POST":
        Quality =  request.POST.get('Quality')
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        amount = int(Quality) * (amount)
        Addtocard_Model.objects.create(userid=userObj,salesid=gymObj, Quality=Quality, day=day, month=month, year=year, amount=amount, requeststatus="PROCESS")
    return render(request,'user/viewmodeldetails.html',{'v':gymObj})

def addtocard(request,pk):
    obj = Addtocard_Model.objects.all()
    return render(request, 'user/addtocard.html', {'objects': obj})

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        productname = request.POST.get('productname')
        feedback = request.POST.get('feedback')
        ratings = request.POST.get('ratings')
        Feeback_Model.objects.create(name=name,productname=productname,ratings=ratings, feedback=feedback)
    return render(request, 'user/feedback.html')


def mydetails(request):
    name = request.session['userid']
    ted = UserRegistration.objects.get(id=name)
    return render(request, 'user/mydetails.html',{'object':ted})


def updatedetails(request):
    name = request.session['userid']
    obj = UserRegistration.objects.get(id=name)
    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        mobilenumber = request.POST.get('mobilenumber', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address','')

        obj = get_object_or_404(UserRegistration, id=name)
        obj.firstname = firstname
        obj.email = email
        obj.password = password
        obj.mobilenumber = mobilenumber
        obj.dob = dob
        obj.gender = gender
        obj.address = address
        obj.save(update_fields=["firstname", "email", "password", "mobilenumber", "dob","gender","address"])
        return redirect('mydetails')


    return render(request, 'user/updatedetails.html',{'form':obj})

def userlogout(request):
    return redirect('userlogin')


def userchart(request,chart_type):

    chart = Feeback_Model.objects.values('productname').annotate(dcount=Avg('ratings'))

    return render(request,"user/userchart.html", {'form':chart, 'chart_type':chart_type})


def reviewspage(request):
    obj = Feeback_Model.objects.all()
    return render(request, 'user/reviewspage.html', {'objects': obj})


def ordertacking(request):
    return render(request,'user/ordertacking.html')

def orderchart(request,schart_type):
    year = 1
    if request.method == "POST":
        year = request.POST.get('year1')


    chart = Addtocard_Model.objects.filter(year=year).values('month').annotate(dcount=Sum('Quality'))

    return render(request,"user/orderchart.html", {'form': chart, 'chart_type':schart_type})


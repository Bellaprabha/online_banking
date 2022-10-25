from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import Customers
from .forms import CustomerForm


# Create your views here.
def homepage(request):
    return render(request,'index.html')
    
def createAccounts(request):
    if request.method=='POST':
        fm=CustomerForm(request.POST)
        if fm.is_valid():
            a =fm.cleaned_data['customerid']
            b =fm.cleaned_data['name']
            c =fm.cleaned_data['Account_no']
            d =fm.cleaned_data['Branch']
            e =fm.cleaned_data['IFSC']
            f =fm.cleaned_data['phone']
            g =fm.cleaned_data['Address']
            reg=Customers(customerid=a,name=b,Account_no=c,Branch=d,IFSC=e,phone=f,Address=g)
            reg.save()
            fm=CustomerForm()

    else:
        fm=CustomerForm()
    m=Customers.objects.all()            


    return render(request,"accounts/createAccounts.html",{'form':fm,'n':m})

def delete(request,id):
    if request.method=='POST':
        de=Customers.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/createAccounts')

def update(request,id):
    if request.method=='POST':
        de=Customers.objects.get(pk=id)
        fm=CustomerForm(request.POST,instance=de)
        if fm.is_valid():
            fm.save()
    else:
        de = Customers.objects.get(pk=id)
        fm = CustomerForm(instance=de)
    return render(request,'update.html',{'form':fm})            


def ShowAcntDetails(request):
    # result= Customers.objects.all():
    if request.method=='POST':
        fm=CustomerForm(request.POST)
        if fm.is_valid():
            a =fm.cleaned_data['customerid']
            b =fm.cleaned_data['name']
            c =fm.cleaned_data['Account_no']
            d =fm.cleaned_data['Branch']
            e =fm.cleaned_data['IFSC']
            f =fm.cleaned_data['phone']
            g =fm.cleaned_data['Address']
            reg=Customers(customerid=a,name=b,Account_no=c,Branch=d,IFSC=e,phone=f,Address=g)
            reg.save()
            fm=CustomerForm()

    else:
        fm=CustomerForm()
    m=Customers.objects.all()


    return render(request,"accounts/createAccounts.html",{'form':fm,'n':m})

    # students = {'allstudents':result}
    return render(request,"accounts/ShowAcntDetails.html")

    

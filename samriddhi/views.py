from django.shortcuts import render
from django.http  import HttpResponse


# Create your views here.


# Create your views here.
def home(request):
	return render(request,'home.html',{'name':'This is from views.py of samriddhi'})

def about(request):
	return render(request,'about.html',{'hello':'This is from views.py of samriddhi of about'})

def add(request):
	val1=int(request.GET['num1'])
	val2=int(request.GET['num2'])
	result=val1+val2
	return render(request,'add.html',{'result':result})

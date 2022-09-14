from django.http.response import HttpResponse
from django.shortcuts import render, redirect 
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

# user pass arun-- arun@112

# Create your views here.

def index(request):
     # print(request.user)
     # if request.user.is_anonymous:
     #      return redirect("/login")
    # context={
    #     "var":"this is index"
    # }
    # return render(request,'index.html', context)           #rendering the templates\
     return render(request,'index.html') 
    

def about(request):
     return render(request,'about.html')
    # return HttpResponse('this is about page')

def EatBetter(request):
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,'EatBetter.html')
    # return HttpResponse('this is services page')

def GetFit(request):
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,'GetFit.html')

def ManageWeight(request):
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,'ManageWeight.html')

def healthtips(request):
     return render(request,'healthtips.html')

def article1(request):
     return render(request,'article1.html')

def Challenges(request):
     if request.user.is_anonymous:
          return redirect("/login")
     return render(request,'Challenges.html')

def pushupchallenge(request):
     return render(request,'pushupchallenge.html')

def plankchallenge(request):
     return render(request,'plankchallenge.html')

def legchallenge(request):
     return render(request,'legchallenge.html')

def burpeechallenge(request):
     return render(request,'burpeechallenge.html')
     
def Cooking(request):
     return render(request,'Cooking.html')

def loginUser(request):
     if request.method=="POST":
          
          username= request.POST.get('username')
          password= request.POST.get('password')
          # print(username,password)
          # check user has entered correct crediantials
          user = authenticate(request, username= username, password= password)
          if user is not None:
              # A backend authenticated the credentials
              login(request, user)
              return redirect("/")
              
              
              
          else:
              # No backend authenticated the credentials
              return render(request,'login.html')

     return render(request,'login.html')

def signupUser(request):
     if request.method=="POST":
          firstname = request.POST.get('firstname')
          lastname = request.POST.get('lastname')
          username = request.POST.get('username')
          password = request.POST.get('password')
          email = request.POST.get('email')

          user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
          user.save()
          return redirect("/login")


     else:
          return render(request,"signup.html")
     

def logoutUser(request):
     logout(request)
     return redirect("/login")

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        desc= request.POST.get('desc')
        contact = Contact(name = name, phone = phone, email = email, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'message has been sent successfully!')

    return render(request,'contact.html')
    # return HttpResponse('this is contact page')
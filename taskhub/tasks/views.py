from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . models import User
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

# Create your views here.

#view for login page 
def IndexPage(request):
    return render(request,"tasks/index.html")

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'tasks/register.html', {'tasks': tasks})

#view for register page 
def RegisterPage(request):
    return render(request,"tasks/register.html")


#view for use registation
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        #first validate the user is allready exist or not
        user = User.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request,"tasks/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Password=password,username=email)
                message = "User Register Successfully"
                return render(request,"tasks/index.html",{'msg':message})
            else:
                message = "Password And Conferm Password Doesnot Match"
                return render(request,"tasks/register.html",{'msg':message})

def DashBoard(request):
    return render(request,"tasks/dashboard.html")

def LoginPage(request):
    return render(request,"tasks/index.html")

# # login user
# def LoginUser(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']

#         #checking emailid in database
#         user = User.objects.get(Email=email)

#         if user:
#             if user.Password == password:
#                 #we are getting user data into session
#                 # request.session['Firstname'] = Users.Firstname
#                 # request.session['Lastname'] = Users.Lastname
#                 # request.session['Email'] = Users.Email
#                 message = "Login Successfull"
#                 return render(request,"tasks/dashboard.html",{'msg':message})
#             else:
#                 message = "Password Does not match"
#                 return render(request,"tasks/index.html",{'msg':message})
#         else:
#             message = "user Does not exist"
#             return render(request,"tasks/register.html",{'msg':message})



def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(Email=email)
        except User.DoesNotExist:
            message = "User does not exist"
            return render(request, "tasks/index.html", {'msg': message})

        if user.Password == password:
            # Start a new session
            request.session['user_id'] = user.id
            return render(request, "tasks/dashboard.html")
        else:
            message = "Password does not match"
            return render(request, "tasks/index.html", {'msg': message})



def LogoutUser(request):
    # End the current session
    request.session.flush()
    return render(request, "tasks/index.html")


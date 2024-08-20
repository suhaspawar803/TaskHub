from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.IndexPage,name="indexpage"),
    path("registerpage/",views.RegisterPage,name="registerpage"),
    path("registeruser/",views.UserRegister,name="registeruser"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    path("logoutuser/",views.LogoutUser,name="logoutuser"),
    #path('index/', views.IndexPage, name='index'),  # Define your index view


]
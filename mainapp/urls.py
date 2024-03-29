"""django_hotel_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name="index"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),
    path('s/', views.search, name="search"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('register/', views.registerView, name="register"),
    path('Student_Record/', views.Student_Record, name="Student_Record"),
    path('Student_Update/<int:pid>', views.Student_Update, name="Student_Update"),
    path('Student_Delete/<int:pid>', views.Student_Delete, name="Student_delete"),
    path('Student_Present/', views.Student_Present, name="Student_Present")
    
     
]

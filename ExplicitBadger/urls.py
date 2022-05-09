"""ExplicitBadger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from TA_Scheduling.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home_admin/', Home_admin.as_view()),
    path('createAccount/', Signup.as_view()),
    path('deleteAccount/', Delete_Account.as_view()),
    path('editAccount/', Edit_Account.as_view()),
    path('createCourse/', Create_Course.as_view()),
    path('createSection/', Create_Section.as_view()),
    path('home_instructor/', Home_instructor.as_view()),
    path('home_ta/', Home_ta.as_view()),
    #path('profile/', User_profile.as_view()),#
]

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
from TA_Scheduling.views import Edit_Account
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('home_admin/', Home_admin.as_view(), name='home_admin'),
    path('createAccount/', Signup.as_view(), name='create_account'),
    path('deleteAccount/', Delete_Account.as_view(), name='delete_account'),
    path('password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success', password_sucess, name="password_success"),
    path('editAccount/', Edit_Account.as_view(), name='edit_account'),
    #path('deleteCourse/', Delete_Account.as_view(), name='delete_course'),
    path('createCourse/', Create_Course.as_view(), name='create_course'),
    path('viewCourse/', View_Course.as_view(), name='view_course'),
    path('viewSection/', View_Section.as_view(), name='view_section'),
    path('createSection/', Create_Section.as_view(), name='create_section'),
    path('home_instructor/', Home_instructor.as_view(), name='home_instructor'),
    path('home_ta/', Home_ta.as_view(), name='home_ta'),
    path('profile/', User_profile.as_view(), name='profile')
]
from django.shortcuts import render, redirect
from django.views import View
from .models import MyUser
from django.contrib import messages
from django.contrib import messages
# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        noSuchUser = False
        badPassword = False
        try:
            m = MyUser.objects.get(name=request.POST['name'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            return render(request, "login.html", {"message": "login failed"})
        elif badPassword:
            return render(request, "login.html", {"message": "bad password"})
        else:
            request.session["name"] = m.name
            print(m.userType)
            if m.userType == 'Admin':
                return redirect("/home_admin/")
            elif m.userType == 'Instructor':
                return redirect("/home_instructor/")
            elif m.userType == 'TA':
                return redirect("/home_ta/")
            else:
                return render(request, "login.html", {"message": "do not have a role"})

class Home_admin(View):
    def get(self, request):
        return render(request, "home_admin.html", {})
    pass

class Signup(View):
    def get(self, request):
        return render(request, "createAccount.html", {})
    pass

class Delete_Account(View):
    def get(self, request):
        return render(request, "deleteAccount.html", {})
    pass

class Edit_Account(View):
    def get(self, request):
        return render(request, "editAccount.html", {})
    pass

class Create_Course(View):
    def get(self, request):
        return render(request, "createCourse.html", {})
    pass

class Create_Section(View):
    def get(self, request):
        return render(request, "createSection.html", {})
    pass

class Home_instructor(View):
    def get(self, request):
        return render(request, "home_instructor.html", {})
    pass

class Home_ta(View):
    def get(self, request):
        return render(request, "home_ta.html", {})
    pass

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

            return redirect("/home_admin/")

class Home_admin(View):
    def get(self, request):
        return render(request, "home_admin.html", {})
    pass

class Signup(View):
    def get(self, request):
        return render(request, "createAccount.html", {})
    pass

class Home_instructor(View):
    def get(self, request):
        return render(request, "home_instructor.html", {})
    pass

class Home_ta(View):
    def get(self, request):
        return render(request, "home_ta.html", {})
    pass

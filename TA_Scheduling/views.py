from django.shortcuts import render, redirect
from django.views import View
from .models import *
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
        m = request.session["name"]
        role = MyUser.objects.get(name=m).userType
        return render(request, "home_admin.html", {"name": m, "role": role})
    pass

class Signup(View):
    def get(self, request):
        return render(request, "createAccount.html", {})

    def post(self, request):
        name = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        userType = request.POST['select_UserType']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        print(name)
        print(pass1)
        print(userType)
        print(email)
        print(fname)
        print(lname)

        if pass1 != pass2:
            return render(request, "createAccount.html", {"message": "Enter same password"})
        else:
            MyUser.objects.create(name=name,password=pass1,userType=userType,email=email,first_name=fname,last_name=lname)
            return render(request, "createAccount.html", {})

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
        all_courses = course.objects.all
        return render(request, "createCourse.html", {"all": all_courses})
    def post(self,request):
        all_courses = course.objects.all
        s = request.POST.get('course','')
        corName = request.session["courseName"]
        corTime = request.session["courseTime"]
        corInstructor = request.session["courseInstructor"]
        secNum = request.session["sectionNum"]
        if s != '':
            newThings = course(courseName= corName,meetingTime=corTime,courseInstructor=corInstructor,sectionNum=secNum)
            newThings.save()
        return render(request, "createCourse.html", {"all": all_courses})

class Create_Section(View):
    def get(self, request):
        return render(request, "createSection.html", {})
    pass

class Home_instructor(View):
    def get(self, request):
        m = request.session["name"]
        role = MyUser.objects.get(name=m).userType
        return render(request, "home_instructor.html", {"name": m, "role": role})
    pass

class Home_ta(View):
    def get(self, request):
        m = request.session["name"]
        role = MyUser.objects.get(name=m).userType
        return render(request, "home_ta.html", {"name": m, "role": role})
    pass

class User_profile(View):
    def get(self, request):
        name = request.session["name"]
        this = MyUser.objects.get(name=name)
        userType = this.userType
        email = this.email
        first_name = this.first_name
        last_name = this.last_name
        return render(request, "profile.html", {"name":name,"role":userType,"email":email,"fName":first_name,"lName":last_name})
    def post(self, request):
        email = request.POST["email"]
        name = request.session["name"]
        this = MyUser.objects.filter(name=name)
        this.update(email=email)
        return redirect("/profile/")

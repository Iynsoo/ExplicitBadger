from django.forms import TimeField
from django.test import TestCase
from .models import MyUser, course, discussion


class AccountCreation(TestCase):
    def test_account_creation(self):
        response = self.client.post("/createAccount/", data={
            "username": "JDoe",
            "pass1": "12345",
            "pass2": "12345",
            "select_UserType": "Admin",
            "email": "someEmail",
            "fname": "John",
            "lname": "Doe"
        })
        self.assertEqual(MyUser.objects.count(), 1)
        self.assertTemplateUsed(response, "createAccount.html")

    def test_account_creation_failure(self):
        response = self.client.post("/createAccount/", data={
            "username": "JDoe",
            "pass1": "12345",
            "pass2": "54321",
            "select_UserType": "Admin",
            "email": "someEmail",
            "fname": "John",
            "lname": "Doe"
        })
        self.assertEqual(MyUser.objects.count(), 0)
        self.assertTemplateUsed(response, "createAccount.html")


class CourseCreation(TestCase):
    def test_course_creation(self):
        response = self.client.post("/createCourse/", data={"courseName": "CompSci", "courseTime": '12:12:12',
                                                            "userID": "", "sectionNum": "123"})
        self.assertEqual(course.objects.count(), 1)
        self.assertTemplateUsed(response, "createCourse.html")

    def test_adding_instructors(self):
        test_instructor1 = MyUser.objects.create(name="JDoe", password="12345", email="someEmail", first_name="John",
                                                 last_name="Doe")
        test_instructor1.userType = "Instructor"
        test_instructor1.save()

        test_instructor2 = MyUser.objects.create(name="BDoe", password="54321", email="someEmail", first_name="Bob",
                                                 last_name="Doe")
        test_instructor2.userType = "Instructor"
        test_instructor2.save()

        response = self.client.post("/createCourse/", data={"courseName": "CompSci", "courseTime": '12:12:12',
                                                            "userID": "1", "sectionNum": "123"})
        self.assertEqual(course.objects.count(), 1)
        self.assertTemplateUsed(response, "createCourse.html")

        response = self.client.post("/createCourse/", data={"courseName": "CompSci", "courseTime": '12:12:12',
                                                            "userID": "2", "sectionNum": "123"})
        self.assertEqual(course.objects.count(), 1)
        self.assertTemplateUsed(response, "createCourse.html")

    def test_course_already_exists(self):
        response = self.client.post("/createCourse/", data={"courseName": "CompSci", "courseTime": '12:12:12',
                                                            "userID": "", "sectionNum": "123"})
        self.assertEqual(course.objects.count(), 1)
        self.assertTemplateUsed(response, "createCourse.html")
        response = self.client.post("/createCourse/", data={"courseName": "CompSci", "courseTime": '12:12:12',
                                                            "userID": "", "sectionNum": "123"})
        self.assertEqual(course.objects.count(), 1)
        self.assertTemplateUsed(response, "createCourse.html")


# class SectionCreation(TestCase):


class Login(TestCase):
    def test_login_admin(self):
        test_admin = MyUser.objects.create(name="JDoe", password="12345", email="someEmail", first_name="John",
                                           last_name="Doe")
        test_admin.userType = "Admin"
        test_admin.save()
        response = self.client.post("/", data={"name": "JDoe", "password": "12345"})
        self.assertRedirects(response, "/home_admin/")

    def test_login_instructor(self):
        test_instructor = MyUser.objects.create(name="JDoe", password="12345", email="someEmail", first_name="John",
                                                last_name="Doe")
        test_instructor.userType = "Instructor"
        test_instructor.save()
        response = self.client.post("/", data={"name": "JDoe", "password": "12345"})
        self.assertRedirects(response, "/home_instructor/")

    def test_login_ta(self):
        MyUser.objects.create(name="JDoe", password="12345", email="someEmail", first_name="John",
                              last_name="Doe")
        response = self.client.post("/", data={"name": "JDoe", "password": "12345"})
        self.assertRedirects(response, "/home_ta/")

    def test_login_no_usertype(self):
        test_user = MyUser.objects.create(name="JDoe", password="12345", email="someEmail", first_name="John",
                                          last_name="Doe")
        test_user.userType = ""
        test_user.save()
        response = self.client.post("/", data={"name": "JDoe", "password": "12345"})
        self.assertTemplateUsed(response, "login.html")

    def test_login_bad_password(self):
        MyUser.objects.create(name="JDoe", password="12345", email="someEmail", first_name="John",
                              last_name="Doe")
        response = self.client.post("/", data={"name": "JDoe", "password": "54321"})
        self.assertTemplateUsed(response, "login.html")

    def test_login_no_such_user(self):
        response = self.client.post("/", data={"name": "JDoe", "password": "12345"})
        self.assertTemplateUsed(response, "login.html")


# class EditAccount(TestCase):


from django.test import TestCase
from .models import MyUser, course, discussion


class TestMyUser(TestCase):
    def test_DefaultUser(self):
        with self.assertRaises(Exception, msg="default constructor fails to raise Exception"):
            m = MyUser()
            m.full_clean()

    def test_DefaultUserType(self):
        m = MyUser(name="Username", password="password", email="email", first_name="firstName", last_name="lastName")
        self.assertEqual("TA", m.userType, msg="Default userType not TA")
        m.full_clean()

    def test_LongUserArgs(self):
        with self.assertRaises(Exception, msg="name is too long (>20)"):
            m = MyUser(name="LoooooooooonoooogUsername", password="password", email="email", first_name="firstName",
                       last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="password is too long (>20)"):
            m = MyUser(name="UserName", password="LooooooooooooooongPassword", email="email", first_name="firstName",
                       last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="userType is too long (>10)"):
            m = MyUser(name="Username", password="password", userType="LooooooooongUserType", email="email",
                       first_name="firstName", last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="email is too long (>40)"):
            m = MyUser(name="Username", password="password", email="LooooooooooooooooooooooooooooooooooooooongEmail",
                       first_name="firstName", last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="first_name is too long (>20)"):
            m = MyUser(name="Username", password="password", email="email",
                       first_name="LooooooooooooooooooongFirstName", last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="last_name is too long (>20)"):
            m = MyUser(name="Username", password="password", email="email", first_name="firstName",
                       last_name="LooooooooooooooooooongLastName")
            m.full_clean()

    def test_NullUserArgs(self):
        with self.assertRaises(Exception, msg="name is null"):
            m = MyUser(name=None, password="password", email="email", first_name="firstName", last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="password is null"):
            m = MyUser(name="Username", password=None, email="email", first_name="firstName", last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="userType is null"):
            m = MyUser(name="Username", password="password", userType=None, email="email", first_name="firstName",
                       last_name=None)
            m.full_clean()

        with self.assertRaises(Exception, msg="email is null"):
            m = MyUser(name="Username", password="password", email=None, first_name="firstName", last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="first_name is null"):
            m = MyUser(name="Username", password="password", email="email", first_name=None, last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="last_name is null"):
            m = MyUser(name="Username", password="password", email="email", first_name="firstName", last_name=None)
            m.full_clean()

    def test_MyUserStr(self):
        m = MyUser(name="Username", password="password", email="email", first_name="firstName",
                   last_name="lastName")
        self.assertEqual(m.__str__(), "firstName lastName")


class TestCourse(TestCase):
    def test_DefaultCourse(self):
        with self.assertRaises(Exception, msg="default constructor fails to raise Exception"):
            m = course()
            m.full_clean()

    def test_LongCourseArgs(self):
        with self.assertRaises(Exception, msg="courseName is too long (>20)"):
            m = course(courseName="LoooooooooonoooogCourse", courseInstructor="Instructor")
            m.full_clean()

        with self.assertRaises(Exception, msg="courseInstructor is too long (>50)"):
            m = course(courseName="Course", courseInstructor="LooooooooooooooooooooooooonoooooooooooooogInstructor")
            m.full_clean()

    def test_NullCourseArgs(self):
        with self.assertRaises(Exception, msg="courseName is null"):
            m = course(courseName=None, courseInstructor="Instructor")
            m.full_clean()

        with self.assertRaises(Exception, msg="courseInstructor is null"):
            m = course(courseName="Course", courseInstructor=None)
            m.full_clean()

    def test_CourseStr(self):
        m = course(courseName="Course", courseInstructor="Instructor")
        self.assertEqual(m.__str__(), "Course")


class TestDiscussion(TestCase):
    def test_DefaultDiscussion(self):
        with self.assertRaises(Exception, msg="default constructor fails to raise Exception"):
            m = discussion()
            m.full_clean()

    def test_LongDiscussionArgs(self):
        with self.assertRaises(Exception, msg="labTA is too long (>50)"):
            m = discussion(labTA="LooooooooooooooooooooooooonoooooooooooooooooooooogTA")
            m.full_clean()

    def test_NullDiscussionArgs(self):
        with self.assertRaises(Exception, msg="labTA is null"):
            m = discussion(labTA=None)
            m.full_clean()

    def test_DiscussionStr(self):
        m = discussion(labTA="TA")
        m.labNum = 123
        self.assertEqual(m.__str__(), "123")


class TestUrlExists(TestCase):
    def test_login_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200, "login/ doesn't exist at desired location")

    def test_home_admin_url(self):
        test_admin = MyUser(name="testAdmin", password="abc", email="admin@email.com", first_name="John",
                            last_name="Doe")
        test_admin.userType = "Admin"
        test_admin.save()

        session = self.client.session
        session['name'] = 'testAdmin'
        session.save()

        response = self.client.get('/home_admin/', session)
        self.assertEqual(response.status_code, 200, "home_admin/ doesn't exist at desired location")

    def test_home_instructor_url(self):
        test_instructor = MyUser(name="testInstructor", password="def", email="instructor@email.com", first_name="Jane",
                                 last_name="Doe")
        test_instructor.userType = "Instructor"
        test_instructor.save()

        session = self.client.session
        session['name'] = 'testInstructor'
        session.save()

        response = self.client.get('/home_instructor/', session)
        self.assertEqual(response.status_code, 200, "home_instructor/ doesn't exist at desired location")

    def test_home_ta_url(self):
        test_ta = MyUser(name="testTA", password="ghi", email="TA@email.com", first_name="Jake",
                         last_name="Doe")
        test_ta.save()

        session = self.client.session
        session['name'] = 'testTA'
        session.save()

        response = self.client.get('/home_ta/', session)
        self.assertEqual(response.status_code, 200, "home_ta/ doesn't exist at desired location")

    def test_createAccount_url(self):
        response = self.client.get('/createAccount/')
        self.assertEqual(response.status_code, 200, "createAccount/ doesn't exist at desired location")

    def test_deleteAccount_url(self):
        response = self.client.get('/deleteAccount/')
        self.assertEqual(response.status_code, 200, "deleteAccount/ doesn't exist at desired location")

    def test_editAccount_url(self):
        response = self.client.get('/editAccount/')
        self.assertEqual(response.status_code, 200, "editAccount/ doesn't exist at desired location")

    def test_createCourse_url(self):
        response = self.client.get('/createCourse/')
        self.assertEqual(response.status_code, 200, "createCourse/ doesn't exist at desired location")

    def test_createSection_url(self):
        response = self.client.get('/createSection/')
        self.assertEqual(response.status_code, 200, "createSection/ doesn't exist at desired location")

    def test_profile_url_exists(self):
        test_ta = MyUser(name="testTA", password="ghi", email="TA@email.com", first_name="Jake",
                         last_name="Doe")
        test_ta.save()

        session = self.client.session
        session['name'] = 'testTA'
        session.save()

        response = self.client.get('/profile/', session)
        self.assertEqual(response.status_code, 200, "profile/ doesn't exist at desired location")


class TestViewUsesCorrectTemplate(TestCase):
    def test_login_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'login.html')

    def test_home_admin_uses_correct_template(self):
        test_admin = MyUser(name="testAdmin", password="abc", email="admin@email.com", first_name="John",
                            last_name="Doe")
        test_admin.userType = "Admin"
        test_admin.save()

        session = self.client.session
        session['name'] = 'testAdmin'
        session.save()

        response = self.client.get('/home_admin/', session)
        self.assertTemplateUsed(response, 'home_admin.html')

    def test_home_instructor_uses_correct_template(self):
        test_instructor = MyUser(name="testInstructor", password="def", email="instructor@email.com", first_name="Jane",
                                 last_name="Doe")
        test_instructor.userType = "Instructor"
        test_instructor.save()

        session = self.client.session
        session['name'] = 'testInstructor'
        session.save()

        response = self.client.get('/home_instructor/', session)
        self.assertTemplateUsed(response, 'home_instructor.html')

    def test_home_ta_uses_correct_template(self):
        test_ta = MyUser(name="testTA", password="ghi", email="TA@email.com", first_name="Jake",
                         last_name="Doe")
        test_ta.save()

        session = self.client.session
        session['name'] = 'testTA'
        session.save()

        response = self.client.get('/home_ta/', session)
        self.assertTemplateUsed(response, 'home_ta.html')

    def test_createAccount_correct_template(self):
        response = self.client.get('/createAccount/')
        self.assertTemplateUsed(response, 'createAccount.html')

    def test_deleteAccount_uses_correct_template(self):
        response = self.client.get('/deleteAccount/')
        self.assertTemplateUsed(response, 'deleteAccount.html')

    def test_editAccount_uses_correct_template(self):
        response = self.client.get('/editAccount/')
        self.assertTemplateUsed(response, 'editAccount.html')

    def test_createCourse_uses_correct_template(self):
        response = self.client.get('/createCourse/')
        self.assertTemplateUsed(response, 'createCourse.html')

    def test_createSection_uses_correct_template(self):
        response = self.client.get('/createSection/')
        self.assertTemplateUsed(response, 'createSection.html')

    def test_profile_uses_correct_template(self):
        test_ta = MyUser(name="testTA", password="ghi", email="TA@email.com", first_name="Jake",
                         last_name="Doe")
        test_ta.save()

        session = self.client.session
        session['name'] = 'testTA'
        session.save()

        response = self.client.get('/profile/')
        self.assertTemplateUsed(response, 'profile.html')


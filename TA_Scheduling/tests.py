from django.test import TestCase
from .models import MyUser, course, discussion


class TestMyUser(TestCase):
    def test_defaultUser(self):
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
                       first_name="firstName",last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="email is too long (>40)"):
            m = MyUser(name="Username", password="password", email="LooooooooooooooooooooooooooooooooooooooongEmail",
                       first_name="firstName",last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="first_name is null"):
            m = MyUser(name="Username", password="password", email="email",
                       first_name="LooooooooooooooooooongFirstName", last_name="lastName")
            m.full_clean()

        with self.assertRaises(Exception, msg="last_name is null"):
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


class TestCourse(TestCase):
    def test_defaultCourse(self):
        with self.assertRaises(Exception, msg="default constructor fails to raise Exception"):
            m = course()
            m.full_clean()

    def test_LongCourseArgs(self):
        with self.assertRaises(Exception, msg="courseName is too long (>20)"):
            m = course(courseName="LoooooooooonoooogCourse", courseInstructor="Instructor")
            m.full_clean()

        with self.assertRaises(Exception, msg="courseInstructor is too long (>20)"):
            m = course(courseName="Course", courseInstructor="LoooooooooonoooogInstructor")
            m.full_clean()

    def test_NullCourseArgs(self):
        with self.assertRaises(Exception, msg="courseName is null"):
            m = course(courseName=None, courseInstructor="Instructor")
            m.full_clean()

        with self.assertRaises(Exception, msg="courseInstructor is null"):
            m = course(courseName="Course", courseInstructor=None)
            m.full_clean()


class TestDiscussion(TestCase):
    def test_defaultCourse(self):
        with self.assertRaises(Exception, msg="default constructor fails to raise Exception"):
            m = discussion()
            m.full_clean()

    def test_LongDiscussionArgs(self):
        with self.assertRaises(Exception, msg="labTA is too long (>20)"):
            m = discussion(labTA="LoooooooooonoooogTA")
            m.full_clean()

    def test_NullDiscussionArgs(self):
        with self.assertRaises(Exception, msg="labTA is null"):
            m = discussion(labTA=None)
            m.full_clean()

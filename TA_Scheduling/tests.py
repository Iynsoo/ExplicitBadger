from django.test import TestCase
from .models import MyUser

class TestMyUser(TestCase):
    def test_NullUserName(self):
        with self.assertRaises(Exception, msg="Username is null"):
            m = MyUser(name=None, password="password")
            m.full_clean()

    def test_LongUserName(self):
        with self.assertRaises(Exception, msg="Username is too long (>20)"):
            m = MyUser(name="LoooooooooonoooogUsername", password="password")
            m.full_clean()

    def test_NullPassword(self):
        with self.assertRaises(Exception, msg="Password is null"):
            m = MyUser(name="Username", password=None)
            m.full_clean()

    def test_LongPassword(self):
        with self.assertRaises(Exception, msg="Password is too long (>20)"):
            m = MyUser(name="Username", password="LooooooooooooooongPassword")
            m.full_clean()

    def test_default(self):
        with self.assertRaises(Exception, msg="default constructor fails to raise Exception"):
            m = MyUser()
            m.full_clean()

    def test_oneArg(self):
        with self.assertRaises(Exception, msg="one argument constructor fails to raise Exception"):
            m = MyUser(name="Username")
            m.full_clean()

    def test_twoArg(self):
        m = MyUser(name="Username", password="password")
        self.assertEqual("username has the password password", m.__str__())
        m.full_clean()

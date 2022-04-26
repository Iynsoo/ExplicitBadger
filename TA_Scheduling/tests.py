from django.test import TestCase
from TA_Scheduling.models import MyUser


class UserTestCase(TestCase):
  def test_default(self):
    with self.assertRaises(TypeError,msg="default constructor fails to raise TypeError"):
      p = MyUser()

  def test_oneArg(self):
    with self.assertRaises(TypeError,msg="one argument constructor fails to raise TypeError"):
      p = MyUser("badger")

  def test_twoArg(self):
    with self.assertRaises(TypeError,msg="two argument constructor fails to raise TypeError"):
      p = MyUser("badger", "password")

  def test_threeArg(self):
    with self.assertRaises(TypeError,msg="three argument constructor fails to raise TypeError"):
      p = MyUser("badger", "password", "badger@school.com")

  def test_fourArg(self):
    p = MyUser("badger", "password", "badger@school.com", 9999999999)
    self.assertEqual("badger has the email badger@school.com and the id of 9999999999", p.__str__())

  def test_fiveArg(self):
    with self.assertRaises(TypeError,msg="five argument constructor fails to raise TypeError"):
      p = MyUser("badger", "password", "badger@school.com", 9999999999, "extra")
import unittest
from django.test import TestCase

from perfectapp.models import Userdata


class Test_login(TestCase):

    def create_whatever(self, title="only a test", body="yes, this is only a test"):
        return Userdata.objects.create(username=title, password=body)

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, Userdata))


if __name__ == '__main__':
    
    unittest.main()
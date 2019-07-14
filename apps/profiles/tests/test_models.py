from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='mehran', password='mehran1234')

    def test_profile(self):
        u = User.objects.first()
        e = Profile.objects.filter(user=u).exists()
        self.assertEqual(e, True)

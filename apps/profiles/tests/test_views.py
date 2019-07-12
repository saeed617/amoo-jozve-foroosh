from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile


class ProfileViewsTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='mehran', password='mehran1234')

    def test_profile(self):
        u = User.objects.first()
        e = Profile.objects.filter(user=u).exists()
        self.assertEqual(e, True)

    def test_users(self):
        req = self.client.post('/profiles/sign-up/', {'email': 'test@test.com',
                                                      'password1': 'testpassword', 'password2': 'testpassword'})
        ln = User.objects.count()
        self.assertEqual(ln, 2)

from django.test import TestCase
from apps.advertise.models import *
from django.contrib.auth.models import User
from apps.advertise.views import *


class AdvertiseViewsTestCase(TestCase):
    def setUp(self):
        u = User.objects.create(username="mehran", password="mehran1234")
        p = Province.objects.create(name="Tehran")
        c = County.objects.create(name="Parand", province=p)
        a = Advertise.objects.create(user=u, county=c, title="test view", description="test description in view", price=1000)
        Comment.objects.create(author=u, advertise=a, text="test cm view")

    def test_advertise(self):
        response1 = self.client.get('/advertise/')
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get('/advertise/1/')
        self.assertEqual(response2.status_code, 200)

    def test_comment(self):
        self.client.login(username='mehran', password='mehran1234')
        post = self.client.post('/advertise/1/add-comment/', {'text': 'new comment creation test'})
        cm_exists = Comment.objects.filter(advertise__id=1).exists()
        self.assertEqual(cm_exists, True)

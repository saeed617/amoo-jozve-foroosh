from apps.advertise.models import Advertise, Comment, County, Province
from django.contrib.auth.models import User
from django.test import TestCase


class AdvertiseTestCase(TestCase):
    def setUp(self):
        u = User.objects.create(username="mehran", password="mehran1234")
        p = Province.objects.create(name='Tehran')
        c = County.objects.create(province=p, name="Pardis")
        a = Advertise.objects.create(user=u, county=c, title="test", description="test description", price=1000)
        Comment.objects.create(advertise=a, author=u, text="great!")

    def test_advertise(self):
        advertise = Advertise.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(advertise.title, advertise.__str__())
        self.assertEqual(user.advertise_set.exists(), True)

    def test_comment(self):
        advertise = Advertise.objects.get(id=1)
        comment = Comment.objects.get(id=1)
        self.assertEqual(advertise.id, comment.advertise_id)
        self.assertEqual(comment.text, "great!")

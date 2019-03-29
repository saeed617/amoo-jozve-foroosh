from django.conf.urls import url
from.views import AdvertiseListView, AdvertiseDetailView

app_name = 'advertise'
urlpatterns = [
    url(r'^$', AdvertiseListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', AdvertiseDetailView.as_view(), name='detail'),
]

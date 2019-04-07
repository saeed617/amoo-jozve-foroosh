from django.conf.urls import url
from . import views

app_name = 'advertise'
urlpatterns = [
    url(r'^$', views.AdvertiseListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AdvertiseDetailView.as_view(), name='detail'),
    url(r'^add/$', views.add_advertise, name='add_advertise'),
]

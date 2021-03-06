from django.conf.urls import url
from . import views

app_name = 'advertise'
urlpatterns = [
    url(r'^$', views.AdvertiseListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.AdvertiseDetailView.as_view(), name='detail'),
    url(r'^add/$', views.AddAdvertise.as_view(), name='add_advertise'),
    url(r'^(?P<pk>[0-9]+)/add-comment/$', views.CommentCreateView.as_view(), name='add_comment'),
    url(r'^ajax/filter-counties/$', views.filter_cities, name='filter-counties'),
    url(r'^rating/(?P<advertise_id>\d+)/$', views.rating, name='rating')
]

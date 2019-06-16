from django.conf.urls import url
from . import views

app_name = 'carts'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.CartDetailView.as_view(), name='detail'),
    url(r'^add-to-cart/$', views.CartCreateView.as_view(), name='add_to_cart'),
    url(r'^remove-from-cart/$', views.CartRemoveView.as_view(), name='remove_from_cart'),
]

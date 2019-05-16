from django.conf.urls import url
from . import views as auth_views

app_name = 'profiles'
urlpatterns = [
    url(r'^login/$', auth_views.authenticate_view, name='login'),
    url(r'^sign-up/$', auth_views.UserCreationView.as_view(), name='sign_up'),
    url(r'^logout/$', auth_views.logout_view, name='logout'),

]

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from .views import UserCreationView, authenticate_view

app_name = 'profiles'
urlpatterns = [
   url(r'^login/$', authenticate_view, name='login'),
   url(r'^sign-up/$', UserCreationView.as_view(), name='sign_up'),

]

from django.conf.urls import url
from django.contrib.auth.views import LoginView

app_name = 'profiles'
urlpatterns = [
   url(r'^login/$', LoginView.as_view(template_name='profiles/login.html'), name='login')
]
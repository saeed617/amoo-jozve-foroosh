from django.conf.urls import url, include
from . import views as auth_views
from django.contrib.auth.views import (PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordResetDoneView, PasswordResetView)

patterns = [
    url(r'^login/$', auth_views.authenticate_view, name='login'),
    url(r'^sign-up/$', auth_views.UserCreationView.as_view(), name='sign_up'),
    url(r'^logout/$', auth_views.logout_view, name='logout'),
    url(r'^activation/$',auth_views.wait_activation, name='activation'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.activate, name='activate'),
    url(r'^my-advertises/$', auth_views.MyAdvertises.as_view(), name='my_advertises'),

]

urlpatterns = [
    url(r'^password-reset/$', PasswordResetView.as_view(
        template_name='profiles/password_reset.html'), name='password_reset'),
    url(r'^password-reset/done$', PasswordResetDoneView.as_view(
        template_name='profiles/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(
        template_name='profiles/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(
        template_name='profiles/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^my-profile/$', auth_views.profile, name='profile'),
    url(r'^', include(patterns, namespace='profiles')),
]
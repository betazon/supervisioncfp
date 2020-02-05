from django.conf.urls import include, url
from .views import(login_view, principal_view, change_pass_view, reset_pass_view, logout_view)

urlpatterns = [
    url(r'^$', login_view, name='login'),
    url(r'^principal/$', principal_view, name='principal'),
    url(r'^change_pass/$', change_pass_view, name='change_pass'),
    url(r'^reset_pass/$', reset_pass_view, name='reset_pass'),
    url(r'^logout/$', logout_view, name='logout'),
]

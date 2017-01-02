from django.contrib.auth.views import login, logout

from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout')
]
from django.conf.urls import url
from django.contrib.auth.views import login, logout

from timentor.forms import LoginForm
from . import views

app_name = 'timentor'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', login, {'template_name': 'timentor/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'timentor/login.html'}, name='logout'),
    url(r'^main/$', views.MainView.as_view(), name='main'),
    url(r'^new_todo/$', views.new_todo_parent, name='new_todo_parent'),
    url(r'^new_todo/(?P<task_date>[0-9]+)/(?P<task_no>[0-9]+)/$', views.new_todo_child, name='new_todo_child'),
    url(r'^list/daily/(?P<task_date>[0-9]+)/edit$', views.list_daily_edit, name="list_daily_edit"),
    url(r'^list/daily/(?P<task_date>[0-9]+)/(?P<task_no>[0-9]+)/edit$',
        views.list_daily_task_edit, name="list_daily_task_edit"),
]

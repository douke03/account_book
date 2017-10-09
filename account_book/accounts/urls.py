from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views
from accounts.forms import LoginForm
from cms.views.todo_view import ToDoView
# from cms.views.todo_view import ToDoView

urlpatterns = [
    url(r'^$', ToDoView.as_view(), name='todo_list'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_save/$', views.register_save, name='register_save'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html',
                             'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', logout, name='logout'),
]

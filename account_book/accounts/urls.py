from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views
from accounts.forms import LoginForm

urlpatterns = [
    url(r'^$', views.root_url, name='root_url'),
    url(r'^register/$', views.CreateUserView.as_view(), name='register'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html',
                             'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', logout, name='logout'),
]

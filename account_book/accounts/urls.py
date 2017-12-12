from django.urls import path
from django.contrib.auth.views import login, logout
from accounts import views
from accounts.forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('', views.root_url, name='root_url'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', login, {'template_name': 'login.html',
                           'authentication_form': LoginForm}, name='login'),
    path('logout/', logout, name='logout'),
]

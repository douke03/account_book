from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^link_list/$', views.link_list, name='link_list'),
    # 書籍
    url(r'^todo/$', views.todo_list, name='todo_list'),
    url(r'^todo/add/$', views.todo_edit, name='todo_add'),
    url(r'^todo/mod/(?P<todo_id>\d+)/$', views.todo_edit, name='todo_mod'),
    url(r'^todo/del/(?P<todo_id>\d+)/$', views.todo_del, name='todo_del'),
]

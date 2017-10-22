from django.conf.urls import url
from cms.views.index import IndexView
from cms.views.todo_view import ToDoView
from cms.views.todo_detail_view import ToDoDatailView
from cms.views.todo_create_view import ToDoCreateView
from cms.views import view

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^todo/$', ToDoView.as_view(), name='todo'),
    url(r'^todo/detail/(?P<pk>\d+)$', ToDoDatailView.as_view(), name='todo_detail'),
    url(r'^todo/create/$', ToDoCreateView.as_view(), name='todo_create'),
    url(r'^todo/add/$', view.todo_edit, name='todo_add'),
    url(r'^todo/mod/(?P<todo_id>\d+)/$', view.todo_edit, name='todo_mod'),
    url(r'^todo/del/(?P<todo_id>\d+)/$', view.todo_del, name='todo_del'),
]

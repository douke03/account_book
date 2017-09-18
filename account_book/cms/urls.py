from django.conf.urls import url
from cms.views.link_list_view import ViewLinkList
from cms.views.todo_view import ViewToDo
from cms.views.todo_detail_view import ViewToDoDatail
from cms.views.todo_create_view import ViewToDoCreate
from cms.views import view

urlpatterns = [
    url(r'^link_list/$', ViewLinkList.as_view()),
    url(r'^todo/$', ViewToDo.as_view(), name='todo_list'),
    url(r'^todo/detail/(?P<pk>\d+)$', ViewToDoDatail.as_view(), name='todo_detail'),
    url(r'^todo/create/$', ViewToDoCreate.as_view(), name='todo_create'),
    url(r'^todo/add/$', view.todo_edit, name='todo_add'),
    url(r'^todo/mod/(?P<todo_id>\d+)/$', view.todo_edit, name='todo_mod'),
    url(r'^todo/del/(?P<todo_id>\d+)/$', view.todo_del, name='todo_del'),
]

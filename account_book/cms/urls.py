from django.conf.urls import url
from cms.views.index import IndexView
from cms.views.todo.todo_list_view import ToDoListView
from cms.views.todo.todo_detail_view import ToDoDatailView
from cms.views.todo.todo_create_view import ToDoCreateView
from cms.views.todo.todo_update_view import ToDoUpdateView
from cms.views.todo.todo_delete_view import ToDoDeleteView
from cms.models.todo_model import ToDo

urlpatterns = [
    url(r'^$',
        IndexView.as_view()),
    url(r'^index/$',
        IndexView.as_view(), name='index'),
    url(r'^todo/$',
        ToDoListView.as_view(), name='todo_list'),
    url(r'^todo/detail/(?P<pk>[\w-]+)$',
        ToDoDatailView.as_view(), name='todo_detail'),
    url(r'^todo/create/$',
        ToDoCreateView.as_view(), name='todo_create'),
    url(r'^todo/edit/(?P<pk>[\w-]+)/$',
        ToDoUpdateView.as_view(model=ToDo), name='todo_update'),
    url(r'^todo/del/(?P<pk>[\w-]+)/$',
        ToDoDeleteView.delete, name='todo_delete'),
]

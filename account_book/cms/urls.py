from django.conf.urls import url
from cms.views.index import IndexView
from cms.views.todo.todo_view import ToDoView
from cms.views.todo.todo_detail_view import ToDoDatailView
from cms.views.todo.todo_create_view import ToDoCreateView
from cms.views.todo.todo_update_view import ToDoUpdateView
from cms.views import view
from cms.models.todo_model import ToDo

urlpatterns = [
    url(r'^$',
        IndexView.as_view()),
    url(r'^index/$',
        IndexView.as_view(), name='index'),
    url(r'^todo/$',
        ToDoView.as_view(), name='todo'),
    url(r'^todo/detail/(?P<pk>\d+)$',
        ToDoDatailView.as_view(), name='todo_detail'),
    url(r'^todo/create/$',
        ToDoCreateView.as_view(), name='todo_create'),
    url(r'^todo/edit/(?P<pk>\d+)/$',
        ToDoUpdateView.as_view(model=ToDo), name='todo_edit'),
    url(r'^todo/del/(?P<todo_id>\d+)/$',
        view.todo_del, name='todo_del'),
]

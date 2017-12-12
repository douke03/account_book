from django.urls import path
from cms.views.index import IndexView
from cms.views.todo.todo_list_view import ToDoListView
from cms.views.todo.todo_detail_view import ToDoDatailView
from cms.views.todo.todo_create_view import ToDoCreateView
from cms.views.todo.todo_update_view import ToDoUpdateView
from cms.views.todo.todo_delete_view import ToDoDeleteView


app_name = 'account_book'
urlpatterns = [
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('todo/', ToDoListView.as_view(), name='todo_list'),
    path('todo/detail/<pk>/', ToDoDatailView.as_view(), name='todo_detail'),
    path('todo/create/', ToDoCreateView.as_view(), name='todo_create'),
    path('todo/edit/<pk>/', ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/del/<pk>/', ToDoDeleteView.delete, name='todo_delete'),
]

from cms.views.common_view import CommonDatailView
from cms.models.todo_model import ToDo


class ToDoDatailView(CommonDatailView):
    template_name = 'cms/todo/todo_detail.html'
    model = ToDo

from cms.views.common_view import CommonDetailView
from cms.models.todo_model import ToDo


class ToDoDatailView(CommonDetailView):
    template_name = 'todo/todo_detail.html'
    model = ToDo

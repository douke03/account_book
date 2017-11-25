from cms.models.todo_model import ToDo
from cms.views.common_view import CommonDetailView


class ToDoDatailView(CommonDetailView):
    template_name = 'todo/todo_detail.html'
    model = ToDo

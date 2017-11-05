from cms.views.common_view import CommonDatailView
from cms.forms.todo.todo_detail_form import ToDoDetailForm


class ToDoDatailView(CommonDatailView):
    template_name = 'cms/todo/todo_detail.html'
    model = ToDoDetailForm

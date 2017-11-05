from django.core.urlresolvers import reverse_lazy
from cms.views.common_view import CommonCreateView
from cms.forms.todo.todo_create_form import ToDoCreateForm


class ToDoCreateView(CommonCreateView):
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('account_book:todo')
    form_class = ToDoCreateForm

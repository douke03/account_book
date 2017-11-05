from django.core.urlresolvers import reverse_lazy
from cms.views.common_view import CommonUpdateView
from cms.forms.todo.todo_update_form import ToDoUpdateForm


class ToDoUpdateView(CommonUpdateView):
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('account_book:todo')
    form_class = ToDoUpdateForm

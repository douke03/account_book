from django.core.urlresolvers import reverse_lazy
from cms.views.common_view import CommonUpdateView
from cms.forms.todo_form import ToDoForm


class ToDoUpdateView(CommonUpdateView):
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('account_book:todo_list')
    form_class = ToDoForm

from django.core.urlresolvers import reverse_lazy
from cms.forms.todo_form import ToDoForm
from cms.views.common_view import CommonCreateView


class ToDoCreateView(CommonCreateView):
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('account_book:todo_list')
    form_class = ToDoForm

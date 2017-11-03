from django.core.urlresolvers import reverse_lazy
from cms.views.common_view import CommonCreateView
from cms.forms.todo.todo_form import ToDoForm


class ToDoCreateView(CommonCreateView):
    template_name = 'cms/todo/todo_create.html'
    success_url = reverse_lazy('account_book:todo')
    form_class = ToDoForm

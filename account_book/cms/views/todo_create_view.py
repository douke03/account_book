from cms.views.common_view import CommonCreateView
from cms.forms import ToDoForm


class ToDoCreateView(CommonCreateView):
    template_name = 'cms/todo_create.html'
    success_url = '/account_book/todo/'
    form_class = ToDoForm

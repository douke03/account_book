from django.views.generic import DetailView
from cms.models.todo_model import ToDo


class ViewToDoDatail(DetailView):
    template_name = 'cms/todo_detail.html'
    model = ToDo

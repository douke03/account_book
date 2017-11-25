from cms.models.todo_model import ToDo
from cms.views.common_view import CommonListView


class ToDoListView(CommonListView):
    template_name = 'todo/todo_list.html'
    model = ToDo

    def get_queryset(self):
        return ToDo.objects.filter(is_active=True).order_by('is_complete', 'priority', 'created_at')

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from cms.models.todo_model import ToDo


@method_decorator(login_required, name='dispatch')
class ViewToDo(ListView):
    template_name = 'cms/todo_list.html'
    model = ToDo
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.object_list = ToDo.objects.filter(
            is_active=True).order_by('is_complete', 'priority', 'id')
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

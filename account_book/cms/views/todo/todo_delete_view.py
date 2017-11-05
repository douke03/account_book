from django.core.urlresolvers import reverse_lazy
from cms.views.common_view import CommonDeleteView
from cms.models.todo_model import ToDo
from django.contrib import messages


class ToDoDeleteView(CommonDeleteView):
    model = ToDo
    success_url = reverse_lazy('account_book:todo')

    def delete(request, pk):
        """ToDoの削除"""

        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete(
            user=User.objects.get(pk=request.user.id),
            now=datetime.now()
        )
        return redirect('account_book:todo')

from django.shortcuts import redirect
from cms.models.todo_model import ToDo
from cms.views.common_view import CommonDelete


class ToDoDeleteView():

    def delete(request, pk):
        view = CommonDelete(model=ToDo)
        is_delete = view.delete(request, pk)
        if is_delete:
            return redirect('account_book:todo_list')
        else:
            return redirect('account_book:todo_list')

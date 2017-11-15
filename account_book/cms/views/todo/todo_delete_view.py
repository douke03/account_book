from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from cms.models.todo_model import ToDo
from datetime import datetime


class ToDoDeleteView():

    def delete(request, pk):
        """ToDoの削除"""

        todo = get_object_or_404(ToDo, pk=pk)
        if todo.is_complete == True:
            todo.delete(
                user=User.objects.get(pk=request.user.id),
                now=datetime.now()
            )
            messages.success(request, '削除しました')
            return redirect('account_book:todo_list')
        else:
            messages.warning(request, '削除できませんでした')
            return redirect('account_book:todo_list')

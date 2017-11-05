from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from cms.models.todo_model import ToDo
from cms.forms.todo.todo_form import ToDoForm


def todo_del(request, todo_id):
    """ToDoの削除"""

    todo = get_object_or_404(ToDo, pk=todo_id)
    todo.delete()

    return redirect('account_book:todo')

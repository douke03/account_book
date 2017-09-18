from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from cms.models.todo_model import ToDo
from cms.forms import ToDoForm


def todo_edit(request, todo_id=None):
    """ToDoの編集"""

    if todo_id:
        todo = get_object_or_404(ToDo, pk=todo_id)
    else:
        todo = ToDo()

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_by = User.objects.get(pk=request.user.id)
            todo.save()
            return redirect('todo_list')
    else:
        form = ToDoForm(instance=todo)

    return render(request, 'cms/todo_edit.html', dict(form=form,
                                                      todo_id=todo_id))


def todo_del(request, todo_id):
    """ToDoの削除"""

    todo = get_object_or_404(ToDo, pk=todo_id)
    todo.delete()

    return redirect('todo_list')

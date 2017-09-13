from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cms.models import ToDoList
from cms.forms import ToDoListForm


def link_list(request):
    """Linkリスト"""

    return render(request, 'cms/link_list.html')


def todo_list(request):
    """ToDoリスト"""

    todo_list = ToDoList.objects.all().order_by('is_complete', 'id')

    return render(request, 'cms/todo_list.html', {'todo_list': todo_list})


def todo_edit(request, todo_id=None):
    """ToDoの編集"""

    if todo_id:
        todo_list = get_object_or_404(ToDoList, pk=todo_id)
    else:
        todo_list = ToDoList()

    if request.method == 'POST':
        form = ToDoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.save()
            return redirect('todo_list')
    else:
        form = ToDoListForm(instance=todo_list)

    return render(request, 'cms/todo_edit.html', dict(form=form, todo_id=todo_id))


def todo_del(request, todo_id):
    """ToDoの削除"""

    todo = get_object_or_404(ToDoList, pk=todo_id)
    todo.delete()

    return redirect('todo_list')

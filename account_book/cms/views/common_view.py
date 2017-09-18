from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from cms.models.todo_model import ToDo
from cms.forms import ToDoForm


class ViewLinkList(TemplateView):

    template_name = "cms/link_list.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        domain = 'http://192.168.10.5:8000/'
        context = {
            'link_todo': domain + 'account_book/todo/',
            'link_admin': domain + 'admin/login/',
            'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        }
        return context


class ViewToDo(ListView):
    template_name = "cms/todo_list.html"
    model = ToDo
    paginate_by = 10

    def get_queryset(self):
        return ToDo.objects.filter(is_active=True).order_by('is_complete', 'id')


class ViewToDoDatail(DetailView):
    template_name = "cms/todo_detail.html"
    model = ToDo


def todo_edit(request, todo_id=None):
    """ToDoの編集"""

    if todo_id:
        todo_list = get_object_or_404(ToDo, pk=todo_id)
    else:
        todo_list = ToDo()

    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo_list)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.save()
            return redirect('todo_list')
    else:
        form = ToDoForm(instance=todo_list)

    return render(request, 'cms/todo_edit.html', dict(form=form,
                                                      todo_id=todo_id))


def todo_del(request, todo_id):
    """ToDoの削除"""

    todo = get_object_or_404(ToDo, pk=todo_id)
    todo.delete()

    return redirect('todo_list')

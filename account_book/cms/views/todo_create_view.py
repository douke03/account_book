from django.views.generic.edit import CreateView
from django.contrib import messages
from cms.forms import ToDoForm


class ViewToDoCreate(CreateView):
    template_name = 'cms/todo_create.html'
    success_url = '/account_book/todo/'
    form_class = ToDoForm

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)

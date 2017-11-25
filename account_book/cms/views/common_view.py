"""viewクラス用の共通定義クラス

viewクラスを作成する際はこのクラス内に定義されているクラスを継承して作成する
共通化すべき定数、変数、メソッドは適宜追加する
特殊な定数、変数、メソッド継承先メソッドに定義する
"""
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@method_decorator(login_required, name='dispatch')
class CommonTemplateView(TemplateView):
    """TemplateViewの共通定義"""

    pass


@method_decorator(login_required, name='dispatch')
class CommonListView(ListView):
    """ListViewクラス用の共通定義"""

    paginate_by = 16


@method_decorator(login_required, name='dispatch')
class CommonDetailView(DetailView):
    """DetailViewの共通定義"""

    pass


@method_decorator(login_required, name='dispatch')
class CommonCreateView(CreateView):
    """CreateViewの共通定義"""

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = User.objects.get(pk=self.request.user.id)
        obj.created_at = datetime.now()
        messages.success(self.request, '登録しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '登録できませんでした')
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class CommonUpdateView(UpdateView):
    """UpdateViewの共通定義"""

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.updated_by = User.objects.get(pk=self.request.user.id)
        obj.updated_at = datetime.now()
        messages.success(self.request, '更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, '更新できませんでした')
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class CommonDeleteView(DeleteView):
    """DeleteViewの共通定義"""

    pass


class CommonDelete():
    """CommonDeleteの共通定義"""

    def __init__(self, *args, **kwargs):
        self.model = kwargs['model']

    def delete(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj.is_complete == True:
            obj.delete(
                user=User.objects.get(pk=request.user.id),
                now=datetime.now()
            )
            messages.success(request, '削除しました')
            return True
        else:
            messages.warning(request, '削除できませんでした')
            return False

"""viewクラス用の共通定義クラス

viewクラスを作成する際はこのクラス内に定義されているクラスを継承して作成する
共通化すべき定数、変数、メソッドは適宜追加する
特殊な定数、変数、メソッド継承先メソッドに定義する
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime


@method_decorator(login_required, name='dispatch')
class CommonTemplateView(TemplateView):
    """TemplateViewクラス用の共通定義"""

    pass


@method_decorator(login_required, name='dispatch')
class CommonListView(ListView):
    """ListViewクラス用の共通定義"""

    paginate_by = 16


@method_decorator(login_required, name='dispatch')
class CommonDetailView(DetailView):
    """DetailViewクラス用の共通定義"""

    pass


@method_decorator(login_required, name='dispatch')
class CommonCreateView(CreateView):
    """CreateViewクラス用の共通定義"""

    def form_valid(self, form):
        """form_valid"""
        obj = form.save(commit=False)
        obj.created_by = User.objects.get(pk=self.request.user.id)
        obj.created_at = datetime.now()
        messages.success(self.request, "登録しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        """form_invalid"""
        messages.warning(self.request, "登録できませんでした")
        return super().form_invalid(form)


@method_decorator(login_required, name='dispatch')
class CommonUpdateView(UpdateView):
    """UpdateViewクラス用の共通定義"""

    def form_valid(self, form):
        """form_valid"""
        obj = form.save(commit=False)
        obj.updated_by = User.objects.get(pk=self.request.user.id)
        obj.updated_at = datetime.now()
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        """form_invalid"""
        messages.warning(self.request, "更新できませんでした")
        return super().form_invalid(form)

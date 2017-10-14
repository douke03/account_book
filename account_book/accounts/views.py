from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import RegisterForm


def root_url(request):

    return redirect('account_book:todo_list')


class CreateUserView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account_book:todo_list')


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', context)

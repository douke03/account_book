from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.forms import RegisterForm


def root_url(request):

    return redirect('account_book:todo')


class CreateUserView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account_book:todo')

    def form_valid(self, form):
        valid = super(CreateUserView, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', context)

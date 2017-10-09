from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from accounts.forms import RegisterForm


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/index.html', context)


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accounts/profile.html', context)


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


@require_POST
def register_save(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('todo_list')

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

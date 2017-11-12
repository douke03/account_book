from cms.models.todo_model import ToDo


def common_process(request):
    context = {
        'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        'link_AdminLTE': 'https://adminlte.io/themes/AdminLTE/index.html',
        'test': ToDo.objects.filter(is_complete=False).count(),
    }
    return context

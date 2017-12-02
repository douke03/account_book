from cms.models.todo_model import ToDo


def common_process(request):

    user = request.user
    unfinished_todo_cnt = get_unfinished_todo_cnt(user)
    unfinished_todo = get_unfinished_todo(user)

    context = {
        'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        'link_AdminLTE': 'https://adminlte.io/themes/AdminLTE/index.html',
        'unfinished_todo_cnt': unfinished_todo_cnt,
        'unfinished_todo': unfinished_todo,
        'remote_ip': request.META['REMOTE_ADDR']
    }
    return context


def get_unfinished_todo_cnt(user):

    if user.is_authenticated:
        obj = ToDo.objects.filter(created_by=user,
                                  is_active=True,
                                  is_complete=False)
        return obj.count()
    else:
        return 0


def get_unfinished_todo(user):

    if user.is_authenticated:
        obj = ToDo.objects.filter(created_by=user,
                                  is_active=True,
                                  is_complete=False)
        return obj.order_by('priority', 'created_at')[:3]
    else:
        return None

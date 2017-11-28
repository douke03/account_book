from cms.models.todo_model import ToDo


def common_process(request):

    unfinished_todo_cnt = ToDo.objects.filter(
        created_by=request.user, is_complete=False).count()
    unfinished_todo = get_unfinished_todo(request)

    context = {
        'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        'link_AdminLTE': 'https://adminlte.io/themes/AdminLTE/index.html',
        'unfinished_todo_cnt': unfinished_todo_cnt,
        'unfinished_todo': unfinished_todo,
        'remote_ip': request.META['REMOTE_ADDR']
    }
    return context


def get_unfinished_todo(request):

    try:
        if request.user.is_superuser:
            return ToDo.objects.filter(
                is_active=True, is_complete=False).order_by('priority', 'created_at')[:3]
        else:
            return ToDo.objects.filter(
                created_by=request.user, is_active=True, is_complete=False).order_by(
                'priority', 'created_at')[:3]
    except:
        return None

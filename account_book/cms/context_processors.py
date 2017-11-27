from cms.models.todo_model import ToDo


def common_process(request):

    try:
        if request.user.is_superuser:
            unfinished_task_cnt = ToDo.objects.filter(
                is_complete=False).count()
            unfinished_task = ToDo.objects.filter(
                is_active=True, is_complete=False).order_by('priority', 'created_at')[:1].get()
        else:
            unfinished_task_cnt = ToDo.objects.filter(
                created_by=request.user, is_complete=False).count()
            unfinished_task = ToDo.objects.filter(
                created_by=request.user, is_active=True, is_complete=False).order_by(
                'priority', 'created_at')[:1].get()
    except:
        unfinished_task_cnt = 0
        unfinished_task = None

    context = {
        'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        'link_AdminLTE': 'https://adminlte.io/themes/AdminLTE/index.html',
        'unfinished_task_cnt': unfinished_task_cnt,
        'unfinished_task_title': unfinished_task,
        'remote_ip': request.META['REMOTE_ADDR']
    }
    return context

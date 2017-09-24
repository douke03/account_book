from django.views.generic import TemplateView


class LinkListView(TemplateView):

    template_name = 'cms/link_list.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        domain = 'http://192.168.10.5:8000/'
        context = {
            'link_todo': domain + 'account_book/todo/',
            'link_admin': domain + 'admin/login/',
            'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        }
        return context

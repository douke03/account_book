from cms.views.common_view import CommonTemplateView


class IndexView(CommonTemplateView):

    template_name = 'cms/index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # domain = 'http://192.168.10.5:8000/'
        domain = 'http://192.168.10.20/'
        context = {
            'link_admin': domain + 'admin/login/',
            'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        }
        return context

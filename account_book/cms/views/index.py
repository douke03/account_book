from cms.views.common_view import CommonTemplateView


class IndexView(CommonTemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context = {
            'link_code': 'https://github.com/douke03/account_book/tree/master/account_book',
        }
        return context

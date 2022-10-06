# from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView

from webapp.models import Article

    
# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.exclude(is_deleted=True)
#         context = {
#             "articles": articles
#         }
#         return render(request, 'index.html', context)

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(is_deleted=False)
        return context

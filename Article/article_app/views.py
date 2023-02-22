from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import ArticleForm


class ArticleView(View):
    def __init__(self):
        super().__init__()

        self.template_name = 'article_app/article.html'

    def get(self, request):
        self.form = ArticleForm()

        self.context = {
            'title': 'Article',
            'form': self.form
        }
        return render(request=request, template_name=self.template_name, context=self.context)

    def post(self, request):
        self.form = ArticleForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return HttpResponse('successful send')

        self.context = {
            'form': self.form
        }
        return render(request=request, template_name=self.template_name, context=self.context)


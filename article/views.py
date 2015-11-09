from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic
from django.db.models import Q

from .models import Article, Category


class HomeListView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Article.published.all()


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'post'
    template_name = 'post.html'


class CategoryView(generic.ListView):
    template_name = 'category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.args[0])
        return Article.published.filter(category=self.category)


class SearchView(generic.ListView):
    model = Article
    template_name = 'category.html'

    def get_queryset(self):
        keyword = self.request.GET.get('s')
        if keyword:
            return Article.published.filter(Q(title__icontains=keyword)|
                                            Q(content__icontains=keyword))
        else:
            return Article.published.all()


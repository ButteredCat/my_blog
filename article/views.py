from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.dates import MonthArchiveView
from django.db.models import Q

from .models import Article, Category


class HomeListView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 6

    def get_queryset(self):
        return Article.published.all()


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'post'
    template_name = 'post.html'

    def get_queryset(self):
        return Article.published.all()


class CategoryView(generic.ListView):
    template_name = 'category.html'
    paginate_by = 20

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.args[0])
        return Article.published.filter(category=self.category)


class SearchView(generic.ListView):
    model = Article
    template_name = 'category.html'
    paginate_by = 20

    def get_queryset(self):
        keyword = self.request.GET.get('s')
        if keyword:
            return Article.published.filter(Q(title__icontains=keyword)|
                                            Q(content__icontains=keyword))
        else:
            return Article.published.all()


class MonthArchiveView(MonthArchiveView):
    queryset = Article.published.all()
    date_field = "date_time"
    template_name = "category.html"
    allow_future = False
    allow_empty = True
    

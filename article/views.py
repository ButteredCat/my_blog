# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.dates import MonthArchiveView, YearArchiveView
from django.views.generic import TemplateView, ArchiveIndexView
from django.db.models import Q

from .models import Article, Category


class HomeListView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 6
    name = u"首页"

    def __unicode__(self):
        return self.name

    def get_queryset(self):
        return Article.published.all()


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = 'post'
    template_name = 'detail.html'

    def get_queryset(self):
        return Article.published.all()

    def __unicode__(self):
        return self.get_object().title


class CategoryView(generic.ListView):
    template_name = 'category.html'
    paginate_by = 20

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.args[0])
        return Article.published.filter(category=self.category)

    def __unicode__(self):
        return u'分类："%s"' % self.args[0] 


class SearchView(generic.ListView):
    model = Article
    template_name = 'category.html'
    paginate_by = 20

    def get_queryset(self):
        self.keyword = self.request.GET.get('s')
        if self.keyword:
            return Article.published.filter(Q(title__icontains=self.keyword)|
                                            Q(content__icontains=self.keyword))
        else:
            return Article.published.all()

    def __unicode__(self):
        return u'搜索"%s"' % self.keyword


class MonthArchiveView(MonthArchiveView):
    queryset = Article.published.all()
    context_object_name = "archives"
    date_field = "date_time"
    template_name = "month_archive.html"
    allow_future = False
    allow_empty = True

    def __unicode__(self):
        return u"按月归档" 


class YearArchiveView(YearArchiveView):
    queryset = Article.published.all()
    context_object_name = "archives"
    date_field = "date_time"
    template_name = "year_archive.html"
    allow_future = False
    allow_empty = True
    make_object_list = True

    def __unicode__(self):
        return u"按年归档" 


class AboutView(TemplateView):
    template_name = "about.html"

    def __unicode__(self):
        return u"关于"


class AllArchiveView(ArchiveIndexView):
    models = Article
    date_field = "date_time"
    queryset = Article.published.all()
    template_name = "archives.html"
    context_object_name = "archives"

    def __unicode__(self):
        return u"归档"


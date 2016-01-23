# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.views.generic import TemplateView

from article.models import Article
from article import views 


info_dict = {
    'queryset': Article.published.all(),
    'date_field': 'last_updated_in',
}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeListView.as_view(), name = 'home'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^archives/$', views.AllArchiveView.as_view(), name = 'archives'),
    url(r'^about/$', views.AboutView.as_view(), name = 'about'),
    url(r'^category/(\w+)/$', views.CategoryView.as_view(), name = 'search_category'),
    url(r'^search/$',views.SearchView.as_view(), name = 'search'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', 
        content_type='text/plain')),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        views.MonthArchiveView.as_view(month_format='%m'), name='month_archive'),
    url(r'^(?P<year>[0-9]{4})/$', views.YearArchiveView.as_view(), 
        name='year_archive'),
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]

admin.site.site_header = u'网站管理'


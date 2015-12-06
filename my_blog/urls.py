from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, ArchiveIndexView

from article.models import Article
from article import views 


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeListView.as_view(), name = 'home'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^archives/$', ArchiveIndexView.as_view(model=Article, template_name='archives.html',
        date_field='date_time', queryset=Article.published.all(),
        context_object_name='archives'), name = 'archives'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name = 'about'),
    url(r'^category/(\w+)/$', views.CategoryView.as_view(), name = 'search_category'),
    url(r'^search/$',views.SearchView.as_view(), name = 'search'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', 
        content_type='text/plain')),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        views.MonthArchiveView.as_view(month_format='%m'), name='month_archive'),
    url(r'^(?P<year>[0-9]{4})/$', views.YearArchiveView.as_view(), 
        name='year_archive'),
]


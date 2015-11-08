from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, ArchiveIndexView

from article.models import Article
from article import views 


urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.HomeListView.as_view(), name = 'home'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    #url(r'^archives/$', views.ArchiveView.as_view(), name = 'archives'),
    url(r'^archives/$', ArchiveIndexView.as_view(model=Article, template_name='archives.html',
        date_field='date_time', queryset=Article.published.all()), name = 'archives'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name = 'about'),
    url(r'^category/(?P<category>\w+)/$', 'article.views.search_category',
        name = 'search_category'),
    url(r'^search/$','article.views.search', name = 'search'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', 
        content_type='text/plain'))
]


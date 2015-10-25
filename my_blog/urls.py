from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView 

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home', name = 'home'),
    url(r'^article/(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^about/$', 'article.views.about', name = 'about'),
    url(r'^category/(?P<category>\w+)/$', 'article.views.search_category',
        name = 'search_category'),
    url(r'^search/$','article.views.search', name = 'search'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', 
    content_type='text/plain'))
]


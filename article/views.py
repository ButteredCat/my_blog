from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

from .models import Article


articles_per_page = 5


# Create your views here.
class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Article.published.all()


def detail(request, id):
    try:
        post = Article.published.get(id=str(id))
    except:
        raise Http404
    return render(request, 'post.html', {'post': post})

def archives(request):
    posts = Article.published.all()
    return render(request, 'archives.html', {'post_list': posts,
                                             'error': False})

def about(request):
    return render(request, 'about.html')

def search_category(request, category):
    try:
        post_list = Article.published.filter_by_category(category)
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'category.html', {'post_list': post_list})

def search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            posts = Article.published.filter(title__icontains=s)
            return render(request, 'archives.html', {'post_list': posts,
                                               'error': len(posts)==0})
    return redirect('/')


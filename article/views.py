from django.shortcuts import render
from django.http import Http404
from django.views import generic

from .models import Article


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
    context_object_name = 'post_list'


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


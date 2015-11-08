from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic

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
    model = Article
    template_name = 'category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, name=self.args[0])
        return Article.published.filter(category=self.category)


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


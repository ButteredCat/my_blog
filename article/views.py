from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article


articles_per_page = 5

def get_published_posts():
    return Article.objects.exclude(is_draft=True)

# Create your views here.
def home(request):
    posts = get_published_posts()
    paginator = Paginator(posts, articles_per_page)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except  EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, id):
    try:
        post = get_published_posts().get(id=str(id))
    except:
        raise Http404
    return render(request, 'post.html', {'post': post})

def archives(request):
    posts = get_published_posts()
    return render(request, 'archives.html', {'post_list': posts,
                                             'error': False})

def about(request):
    return render(request, 'about.html')

def search_tag(request, tag) :
    try:
        post_list = get_published_posts().filter(category__iexact=tag)
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})

def search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            posts = get_published_posts().filter(title__icontains=s)
            return render(request, 'archives.html', {'post_list': posts,
                                               'error': len(posts)==0})
    return redirect('/')


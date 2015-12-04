from django.db.models import Count
from .models import Category

def category(request):
    category = Category.objects.annotate(num_article=Count('article'))
    return {'categories': category,}
    

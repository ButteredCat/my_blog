from sets import Set

from django.db.models import Count
from .models import Category, Article


def category(request):
    category = Category.objects.filter(article__is_draft=False).annotate(
            num_article=Count('article'))
    return {'categories': category,}
   
def month_list(request):
    articles = Article.published.all()
    year_month = Set()
    for each in articles:
        year_month.add((each.date_time.year, each.date_time.month))
    year_month = list(year_month)
    year_month.sort(reverse=True)
    return {'year_month': year_month,}


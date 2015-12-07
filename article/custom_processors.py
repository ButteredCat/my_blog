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
    counter = {}.fromkeys(year_month, 0)    # counter = {(year, month):0, ... }
    for each in articles:
        counter[(each.date_time.year, each.date_time.month)] += 1
    year_month_counter = []
    for key in counter:
        year_month_counter.append([key[0], key[1], counter[key]]) 
    year_month_counter.sort(reverse=True)   # {[year, month, counter], ... }
    return {'year_month_counter': year_month_counter,}

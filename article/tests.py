import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Article, Category

def create_category(name):
    return Category.objects.create(name)

def get_category_by_name(name):
    return Category.objects.get(name=name)

def create_article(title, days, is_draft=False, category_name='test', content='default'):
    pub_time = timezone.now() + datetime.timedelta(days=days) 
    try:
        category = get_category_by_name(name)
    except Category.DoesNotExist:
        category = create_category(name) 
    return Article.objects.create(title=title, date_time=pub_time,
        is_draft=is_draft, content=content, category=category)


class ArticleDetailViewTests(TestCase):
    def should_not_have_access_to_draft(self):
        draft = create_article('test title', -1, True)
        response = self.client.get(reverse('article', args=(draft.id,)))
        self.assertEqual(response.status_code, 404)





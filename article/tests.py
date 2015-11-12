import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Article, Category

def create_category(name):
    return Category.objects.create(name=name)

def get_category_by_name(name):
    return Category.objects.get(name=name)

def create_article(title, days, is_draft=False, category_name='test', content='default'):
    pub_time = timezone.now() + datetime.timedelta(days=days) 
    try:
        category = get_category_by_name(category_name)
    except Category.DoesNotExist:
        category = create_category(category_name) 
    return Article.objects.create(title=title, date_time=pub_time,
        is_draft=is_draft, content=content, category=category)


class ArticleDetailViewTests(TestCase):
    published = None
    draft = None

    def setUp(self):
        self.published = create_article('published article', -1, False, 'test',
                'test article')
        self.draft = create_article('draft', -1, True)
        
    def test_should_have_access_to_published(self):
        response = self.client.get(reverse('detail', args=(self.published.id,)))
        self.assertEqual(response.status_code, 200)

    def test_should_contain_title(self):
        response = self.client.get(reverse('detail', args=(self.published.id,)))
        self.assertContains(response, self.published.title)

    def test_should_contain_content(self):
        response = self.client.get(reverse('detail', args=(self.published.id,)))
        self.assertContains(response, self.published.content)

    def test_should_contain_category(self):
        response = self.client.get(reverse('detail', args=(self.published.id,)))
        self.assertContains(response, self.published.category.name)

    def test_should_not_have_access_to_draft(self):
        response = self.client.get(reverse('detail', args=(self.draft.id,)))
        self.assertEqual(response.status_code, 404)


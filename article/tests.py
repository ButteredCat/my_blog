import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Article, Category


def create_category(name):
    return Category.objects.create(name=name)

def get_category_by_name(name):
    return Category.objects.get(name=name)

def create_article(title, days, content='default', category_name='test',
        is_draft=False):
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
        self.published = create_article('published article', -1, 'test article')
        self.draft = create_article('draft', -1, 'editing', 'test', True)
        
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


class ArticleCategoryViewTests(TestCase):
    category1 = []
    category_name = 'catgory_one'

    def setUp(self):
        for i in range(5):
            title = 'article %d' % i
            self.category1.append(create_article(title, -i, 'default',
                self.category_name))

    def test_should_get_404_when_category_does_not_exist(self):
        response = self.client.get(reverse('search_category',
            args=('notexist',)))
        self.assertEqual(response.status_code, 404)

    def test_should_get_article_when_access_category(self):
        response = self.client.get(reverse('search_category',
            args=(self.category_name,)))
        for i in range(len(self.category1)):
            self.assertContains(response, self.category1[i].title)

    def test_should_not_get_draft(self):
        draft = create_article('draft', -1, 'nothing', self.category_name, True)
        self.category1.append(draft)
        response = self.client.get(reverse('search_category',
            args=(self.category_name,)))
        self.assertNotContains(response, draft.title)


class ArticleArchiveViewTests(TestCase):
    articles = []

    def setUp(self):
        for i in range(5):
            title = 'article %d' % i
            self.articles.append(create_article(title, -i))

    def test_should_get_article_when_access_archive(self):
        response = self.client.get(reverse('archives'))
        for i in range(len(self.articles)):
            self.assertContains(response, self.articles[i].title)
        
    def test_should_not_get_draft(self):
        draft = create_article('draft', -1, 'nothing', 'django', True)
        self.articles.append(draft)
        response = self.client.get(reverse('archives'))
        self.assertNotContains(response, draft.title)
        

class ArticleSearchViewTests(TestCase):
    keyword = ['django', 'python', 'github']
    published = [] 
    draft = None

    def setUp(self):
        self.published = [create_article(self.keyword[0], -1),
                create_article('any but keyword', -1, self.keyword[1])]
        self.draft = create_article(self.keyword[2], -1, 'to be, or not to be',
                'test', True)

    def test_should_get_results_when_search_title(self):
        response = self.client.get(reverse('search'), {'s': self.keyword[0]})
        self.assertContains(response, self.published[0].title)

    def test_should_get_results_when_search_content(self):
        response = self.client.get(reverse('search'), {'s': self.keyword[1]})
        self.assertContains(response, self.published[1].title)

    def test_should_not_get_draft(self):
        response = self.client.get(reverse('search'), {'s': self.keyword[2]})
        self.assertNotContains(response, self.draft.content)

    def test_should_get_all_published_when_keyword_is_null(self):
        response = self.client.get(reverse('search'), {'s': ''})
        self.assertContains(response, self.published[0].content) 
        self.assertContains(response, self.published[1].content) 
        self.assertNotContains(response, self.draft.content) 


from django.test import TestCase, Client
from django.urls import reverse

from .models import Post, Author
from .views import PostsView, PostsDetailView

class PostsViewTestCase(TestCase):
    def test_get(self):
        c = Client()
        response = c.get(reverse('api:posts'))

        self.assertEqual(response.status_code, 200)

    def test_empty_post(self):
        c = Client()
        response = c.post(reverse('api:posts'), {}, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_post(self):
        a = Author.objects.create(name='Humberto')

        c = Client()

        post_body = {
            'title': 'Django is a great backend framework',
            'content': 'Python is one of the most beloved programming languages...',
            'author': a.id,
        }

        response = c.post(reverse('api:posts'), post_body, content_type='application/json')
        self.assertEqual(response.status_code, 201)

class PostsDetailViewTestCase(TestCase):
    def create_test_post(self):
        a = Author.objects.create(name='Humberto')

        p = Post.objects.create(
            title='Django is a great backend framework',
            content='Python is one of the most beloved programming languages...',
            author=a,
        )

        return p

    def test_get(self):
        p = self.create_test_post();
        c = Client()

        response = c.get(reverse('api:posts_detail', args=(p.pk,)))
        self.assertEqual(response.status_code, 200)
from http import HTTPStatus

from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_url1_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_url2_exists_at_desired_location(self):
        response = self.guest_client.get('/second/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_page1_shows_correct_content(self):
        """Проверка контента страниц."""
        response = self.guest_client.get('/')
        self.assertContains(response, 'У меня получилось!')

    def test_page2_shows_correct_content(self):
        response = self.guest_client.get('/second/')
        self.assertContains(response, 'А это вторая страница')

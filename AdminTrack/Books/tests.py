from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Book
from .forms import BookForm
from .views import admin_login, admin_logout, view_books, add_book, edit_book, delete_book


# Create your tests here.
class BookTestCase(TestCase):
    """
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='password')
        self.book = Book.objects.create(name='Sam Peter', subject='English')

    def test_admin_login_view(self):
        response = self.client.post(reverse('admin_login'), {'username': 'admin', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_admin_logout_view(self):
        self.client.force.login(self.user)
        response = self.client.get(reverse('admin_logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
    """

    def test_view_books(self):
        self.client.login(username='admin', password='admin12')
        response = self.client.get(reverse('view_books'))
        self.assertEqual(response.status_code, 200)

    def test_edit_list(self):
        self.client.login(username='admin', password='admin12')
        response = self.client.get(reverse('edit_book', args=[self.book.id]),{'title': 'Edited Book', 'author': 'Mary Jane'})
        self.assertEqual(response.status_code, 302)

    def test_delete_book(self):
        self.client.login(username='admin', password='admin12')
        response = self.client.get(reverse('delete_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)

    def test_add_book(self):
        self.client.login(username='admin', password='admin12')
        response = self.client.get(reverse('add_book'), {'title': 'New Book', 'author': 'Mary Jane'})
        self.assertEqual(response.status_code, 302)

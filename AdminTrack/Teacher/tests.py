from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Teacher
from .forms import TeacherForm
from .views import view_teachers, add_teacher, edit_teacher, delete_teacher


# Create your tests here.
class TestViews(TestCase):
    """
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='password')
        self.teacher = Teacher.objects.create(name='Sam Peter', subject='English')

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

    def test_view_teachers_view(self):
        self.client.force.login(self.user)
        response = self.client.get(reverse('view_teachers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teachers/view_teachers.html')

    def test_edit_teacher_view(self):
        self.client.force.login(self.user)
        response = self.client.get(reverse('edit_teacher', args=[self.teacher.id]), {'name': 'Sam Peters', 'subject': 'Physics'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_teachers'))

    def test_delete_teacher_view(self):
        self.client.force.login(self.user)
        response = self.client.get(reverse('delete_teacher', args=[self.teacher.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_teachers'))

    def test_add_teacher_view(self):
        self.client.force.login(self.user)
        response = self.client.get(reverse('add_teacher'), {'name': 'Mercy Chep', 'subject': 'Science'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_teachers'))

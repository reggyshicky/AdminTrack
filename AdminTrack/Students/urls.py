from django.urls import path
from . import views
from .views import login, logout

urlpatterns = [
    path('view_students/', views.view_students, name="view_students"),
    path('view_students/add/', views.add_student, name='add_student'),
    path('view_students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('view_students/delete/<int:id>/', views.delete_student, name="delete_student")
]

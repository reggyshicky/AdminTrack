from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/add", views.add_student, name="add_student"),
    path("students/<int:pk>", views.student_detail, name="student_detail"),
    path("books/", views.book_list, name="book_list"),
    path("books/add", views.add_book, name="add_book"),
    path("books/<int:pk>", views.book_detail, name="book_detail"),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("teachers/add", views.add_teacher, name="add_teacher"),
    path("teachers/<int:pk>", views.teacher_detail, name="teacher_detail"),
]
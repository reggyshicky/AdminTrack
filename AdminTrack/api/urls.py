from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/add", views.post_student, name="post_student"),
    path("students/<int:pk>", views.student_detail, name="student_detail"),
    path("books/", views.book_list, name="book_list"),
    path("books/add", views.add_book, name="add_book"),
    path("books/<int:pk>", views.book_detail, name="book_detail"),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("teachers/add", views.add_teacher, name="add_teacher"),
    path("teachers/<int:pk>", views.teacher_detail, name="teacher_detail"),
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/add", views.post_employee, name="post_student"),
    path("employees/<int:id>", views.employee_details, name="employee_details"),
    path("attendance_list/", views.attendance_list, name="attendance_list"),
    path("attendance_list/add", views.post_attendance, name="post_attendance"),
    path("attendance_list/<int:id>", views.attendance_details, name="attendance_details")
    
]
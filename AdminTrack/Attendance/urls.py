from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_attendance, name="list_attendance"),
    path('list/create_attendance/', views.create_attendance, name="create_attendance"),
    path('list/update_attendance/<int:attendance_id>/', views.update_attendance, name="update_attendance"),
    path('list/delete_attendance_record/<int:attendance_id>/', views.delete_attendance_record, name="delete_attendance_record"),
    path('list/by_status/', views.list_attendance_by_status, name="list_attendance_by_status"),
]
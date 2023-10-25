from . import views
from django.urls import path

urlpatterns = [
    path('view_employees/', views.view_employees, name="view_employees"),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:id>/', views.edit_employee, name="edit_employee"),
    path('delete_employee/<int:id>/', views.delete_employee, name="delete_employee"),
]
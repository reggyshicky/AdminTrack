from django.urls import path
from . import views
#from .views import login, logout
app_name = "Teacher"
urlpatterns = [
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('edit/teacher/<int:pk>', views.modified, name="modified"),
    # path('edit_teachers/edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers', views.view_teachers, name='view_teachers'),
    path('create', views.create, name='create'),
    path('delete_teachers/delete/<int:id>/', views.delete_teacher, name='delete_teacher'),
]

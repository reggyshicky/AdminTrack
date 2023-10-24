from django.urls import path
from . import views
#from .views import login, logout

urlpatterns = [
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('view_teachers', views.view_teachers, name='view_teachers'),
    path('view_teachers/add/', views.add_teacher, name='add_teacher'),
    path('view_teachers/edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('view_teachers/delete/<int:id>/', views.delete_teacher, name='delete_teacher'),
]

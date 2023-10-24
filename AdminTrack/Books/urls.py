from django.urls import path
from . import views
#from .views import login, logout

urlpatterns = [
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('view_books', views.view_books, name='view_books'),
    path('view_books/add/', views.add_book, name='add_book'),
    path('view_books/edit/<int:id>/', views.edit_book, name='edit_book'),
    path('view_books/delete/<int:id>/', views.delete_book, name='delete_book'),
]
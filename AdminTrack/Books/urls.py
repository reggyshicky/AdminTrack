from django.urls import path
from . import views
#from .views import login, logout
app_name = "Books"
urlpatterns = [
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('view_books', views.view_books, name='view_books'),
    path('add', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('view_books/delete/<int:id>/', views.delete_book, name='delete_book'),
]
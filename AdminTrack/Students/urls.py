from django.urls import path
from . import views

urlpatterns = [
    path('studentPage', views.view_student, name="studentPage"),
    path('', views.homepage, name="homepage"),
]

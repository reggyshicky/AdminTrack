from django.urls import path
from . import views

urlpatterns = [
    path('studentPage', views.student, name="studentPage"),
    path('', views.homepage, name="homepage"),
]

from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path('checkin/', views.checkin, name="checkin")
  path('snake/', views.snake, name="snake"),
  path('action/', views.action, name="action")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('verify/', views.verify_code, name='verify_code'),
]





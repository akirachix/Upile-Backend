from django.urls import path
from .views import login_user, verify_otp
from .import views


urlpatterns = [
    path('login/', login_user, name='login'),
    path('verify-otp/', verify_otp, name='verify_otp'),
]
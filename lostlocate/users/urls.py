from django.urls import path
from users.views import login_user, user_register, verify_code, verify_otp

urlpatterns = [
    path("login/", login_user, name="login"),
    path("verify-otp/", verify_otp, name="verify_otp"),
    path("register/", user_register, name="register"),
    path("verify-code/", verify_code, name="verify_code"),
]

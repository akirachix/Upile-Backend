from django.urls import path
from users.views import login_user, user_register, verify_sms_otp

urlpatterns = [
    path("login/", login_user, name="login"),
    # path("verify-otp/", verify_otp, name="verify_otp"),
    path("register/", user_register, name="register"),
    path("verify-sms-code/", verify_sms_otp, name="verify-sms-code"),
]

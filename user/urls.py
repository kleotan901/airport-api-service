from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from user.views import CreateUserView, ManageUserView, SendEmailConfirmationAPIView

app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path(
        "email-confirmation/",
        SendEmailConfirmationAPIView.as_view({"post": "post"}),
        name="email-confirmation",
    ),
    path(
        "email-verification/",
        SendEmailConfirmationAPIView.as_view({"post": "email_verification"}),
        name="email-verification",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

from django.urls import path

from .views import SigninView, SignupView

app_name = "user"

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
    path("signin", SigninView.as_view(), name="signin"),
]

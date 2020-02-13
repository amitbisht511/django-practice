from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView

# Create your views here.


class SignupView(CreateView):
    template_name = "users/signup.html"
    model = User
    fields = ["first_name", "last_name", "email", "username", "is_active", "password"]
    # fields = "__all__"


class SigninView(TemplateView):
    template_name = "users/signin.html"

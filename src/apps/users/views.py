from django.views.generic import TemplateView

# Create your views here.


class SignupView(TemplateView):
    template_name = "users/signup.html"


class SigninView(TemplateView):
    template_name = "users/signin.html"

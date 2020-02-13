from django.forms import ModelForm


class SignupForm(ModelForm):
    fields = "__all__"

from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View, TemplateView


class LoginForm(AuthenticationForm, View):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password'].widget.attrs['class'] = 'input'

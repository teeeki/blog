from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .form import LoginForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm  # フォームクラス「LoginForm」を指定
    template_name = 'accounts/login.html'   # 使用するテンプレート（HTML）


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'   # ログアウト後に表示されるテンプレート（HTML）


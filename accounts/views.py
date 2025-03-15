from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .form import LoginForm, SignUpForm
from django.contrib.auth import login
from django.urls import reverse_lazy


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm  # フォームクラス「LoginForm」を指定
    template_name = 'accounts/login.html'   # 使用するテンプレート（HTML）


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'   # ログアウト後に表示されるテンプレート（HTML）


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect(self.get_success_url())
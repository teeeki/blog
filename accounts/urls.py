from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path("login/", views.Login.as_view(), name='login'),
    path("blog/login/", views.Login.as_view(), name='login'),
    path("blog/logout/", views.Logout.as_view(), name='logout'),
    path("blog/signup/", views.SignUp.as_view(), name='signup'),
]

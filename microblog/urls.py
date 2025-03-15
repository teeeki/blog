from django.contrib import admin
from django.urls import path
from django.urls import path, include
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('accounts.urls')),
    path("blog/", views.FrontPageView.as_view(), name="frontpage"),
    path("post/<int:id>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<str:post_id>/like/", views.PostLike.as_view(), name="post_like"),

]

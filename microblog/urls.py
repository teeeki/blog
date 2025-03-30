from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.views.generic.base import RedirectView
from blog import views

app_name = 'blog'

urlpatterns = [
    path("blog/admin/", admin.site.urls),
    path("", include('accounts.urls')),
    path("", RedirectView.as_view(url="blog/login/", permanent=False)),     # ルートにアクセス時にリダイレクト
    path("blog/top", views.FrontPageView.as_view(), name="top"),
    path("blog/post/<int:id>/", views.PostDetailView.as_view(), name="post_detail"),
    path("blog/post/<str:post_id>/like/", views.PostLike.as_view(), name="post_like"),
    # 新規投稿用webページのURL
    path("blog/newpost", views.NewPost.as_view(), name="newpost"),
    # 新規投稿をDBに格納
    path("blog/savepost", views.SavePost.as_view(), name="savepost"),
    
]

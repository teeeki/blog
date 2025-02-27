from django.contrib import admin
from django.urls import path
# from blog.views import frontpage
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog", views.frontpage),
    path("<slug:slug>/", views.post_detail, name="post_detail")
]

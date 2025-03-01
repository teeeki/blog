from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
# from django.views import View
from .models import Post, Likes
from blog.forms import CommentForm


class FrontPageView(TemplateView):
    template_name = "blog/frontpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context



class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        
        # いいね数といいねしたユーザの取得
        likes_count = Likes.objects.filter(post=post).count()
        liked_users = Likes.objects.filter(post=post).select_related('user')
        
        return render(
            request, 
            "blog/post_detail.html", 
            {
                "post": post,
                "form": form,
                "likes_count": likes_count,
                "liked_users": liked_users
                }
            )


    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=slug)

        # いいね数といいねしたユーザの取得
        likes_count = Likes.objects.filter(post=post).count()
        liked_users = Likes.objects.filter(post=post).select_related('user')

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "form": form,
                "likes_count": likes_count,
                "liked_users": liked_users
            }
        )

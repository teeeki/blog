from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
# from django.views import View
from .models import Post
from blog.forms import CommentForm


# def frontpage(request):
#     posts = Post.objects.all()
#     return render(request, "blog/frontpage.html", {"posts": posts})
class FrontPageView(TemplateView):
    template_name = "blog/frontpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


# def post_detail(request, slug):
#     post = Post.objects.get(slug=slug)
    
#     if request.method == "POST":
#         form = CommentForm(request.POST)
        
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
            
#             return redirect("post_detail", slug=post.slug)
    
#     else:
#         form = CommentForm()
    
#     return render(request, "blog/post_detail.html", {"post": post, "form": form})
class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        return render(request, "blog/post_detail.html", {"post": post, "form": form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=slug)

        return render(request, "blog/post_detail.html", {"post": post, "form": form})

from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, RedirectView
from .models import Post, Like
from blog.forms import CommentForm
from django.http import JsonResponse
from .forms import ArticleForm
from django.views.generic.edit import FormView
from django.utils.text import slugify


class FrontPageView(TemplateView, RedirectView):
    template_name = "blog/frontpage.html"
    pattern_name = "post_detail"    # リダイレクト先URLのname

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context



class PostDetailView(View):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        form = CommentForm()
        
        # いいね数といいねしたユーザの取得
        likes_count = Like.objects.filter(post=post).count()
        liked_users = Like.objects.filter(post=post).select_related('user')
        
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

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", id=id)

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


class PostLike(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        # すでに「いいね」していた場合は解除
        if not created:
            like.delete()

        # 「いいね」の数を返す
        return JsonResponse({'likes_count': Like.objects.filter(post=post).count()})
    
    
class NewPost(FormView):
    template_name = "blog/newpost.html"
    form_class = ArticleForm
    success_url = "top"


class SavePost(TemplateView):
    template_name = "blog/newpost.html"
    form_class = ArticleForm

    def get(self, request):
        print(request.user)
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        print(request.user)
        form_data = self.form_class(request.POST)
        if form_data.is_valid():
            try:
                post = form_data.save(commit=False)
                post.user = request.user  # ← 忘れがちなポイント！
                post.slug = slugify(post.title)  # ← slugの重複にも注意
                post.save()
                return redirect("top")
            except Exception as e:
                print("保存エラー:", e)
                form_data.add_error(None, "保存時にエラーが発生しました。")
        return render(request, self.template_name, {"form": form_data})
    
    

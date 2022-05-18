from audioop import reverse
from operator import ne
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm
from django.views import generic
from django.views import View
from django.views.generic import ListView
# Create your views here.


# class IndexPageView(ListView):
#     class Meta:
#         model: Post
#         template_name = "blog/index.html"
#         context_object_name: "posts"
#     queryset = Post.objects.all()
#     # ordering: ["-date"]

#     def get_queryset(self):
#         query = super().get_queryset()
#         data = query[:3]
#         return data

def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    allposts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', {
        "allposts": allposts
    })


# def post_detail(request, slug):
#     if request.method == "GET":
#         identified_post = get_object_or_404(Post, slug=slug)
#         comments_form = CommentForm()
#         return render(request, "blog/post-detail.html", {
#             "post": identified_post,
#             "comments_form": comments_form
#         })

#     if request.method == "POST":
#         comment_form = CommentForm(request.POST)
#         post = Post.objects.get(slug=slug)

#         if comment_form.is_valid():
#             # comment_form.save()
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#             return HttpResponseRedirect(reverse("one_post", args=slug))

#         context = {
#             "post": post,
#             "comment_form": comment_form
#         }

#         return render(request, "blog/post-detail.html", context)

class SingePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            # comment_form.save()
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse("one_post", args=[slug]))

        context = {
            "post": post,
            "comment_form": comment_form,
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)

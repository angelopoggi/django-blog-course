from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Post, PostComments
from .forms import CommentsForm

#TODO: add a comment section with Forms
#TODO: add a Read Later Feature with Sessions
#TODO: Adding file uploads (post images)

class StartingPage(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-post_date"]
    #by default django uses the name objectList
    context_object_name = "posts"

    #this is how we get the data
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    order = ["-post_date"]
    context_object_name = "all_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class PostDetailsView(View):
    template_name = "blog/post-detail.html"
    model = Post
    slug_field = "post_slug"

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(post_slug=slug)
        context = {
            "post": post,
            "post_tags": post.post_tag.all(),
            "comment_form" : CommentsForm(),
            "comments" : post.comments.all().order_by("-id"),
            "save_for_later" : self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentsForm(request.POST)
        post = Post.objects.get(post_slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.post_tag.all(),
            "comment_form": CommentsForm(),
            "comments": post.comments.all().order_by("-id"),
            "save_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = []
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []
        if int(request.POST["post_id"]) not in stored_posts:
            stored_posts.append(int(request.POST["post_id"]))
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(int(request.POST["post_id"]))
            request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")








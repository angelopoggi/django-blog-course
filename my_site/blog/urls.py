from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    #dyanamic path <>
    #also called a "slug" i.e podjang/my-post
    #slug:slug built in modifier alllows int and str no special characters
    path("posts/<slug:slug>", views.PostDetailsView.as_view(), name="post-details-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]

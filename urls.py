from django.shortcuts import get_object_or_404, redirect
from django.urls import path
from . import views
from .models import Post

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
path('drafts/', views.post_draft_list, name='post_draft_list'),

path('post/<pk>/publish/', views.post_publish, name='post_publish'),


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

path('post/<pk>/remove/', views.post_remove, name='post_remove'),

path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

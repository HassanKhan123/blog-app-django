from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class StartingPageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'all_posts'
    ordering = ['-date']


class SinglePostView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tags.all()
        return context

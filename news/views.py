from datetime import datetime

from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-post_datetime', ]


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsitem.html'
    context_object_name = 'newsitem'

from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    template_name = "news.html"
    context_object_name = "news"
    ordering = ["-post_datetime"]
    paginate_by = 1

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsitem.html'
    context_object_name = 'newsitem'

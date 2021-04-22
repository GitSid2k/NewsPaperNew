from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ('post_title', 'posts', 'post_datetime', 'post_category')

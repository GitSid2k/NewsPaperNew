from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'post_title': ['icontains'],
            'post_datetime': ['gt'],
            'author': ['exact'],
            'post_category': ['exact'],
            'post_content': ['icontains'],
        }


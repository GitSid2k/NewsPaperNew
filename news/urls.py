from django.urls import path

from .views import PostList, PostCreateView, PostDetailView

from django.conf.urls import url
from django_filters.views import object_filter
from news.models import Post

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    # path('<int:pk>', NewsDetail.as_view()),
    url(r'^list/$', object_filter, {'model': Post}),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]

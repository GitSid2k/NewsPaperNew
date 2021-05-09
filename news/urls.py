from django.urls import path

from .views import PostList, NewsDetail

from django.conf.urls import url
from django_filters.views import object_filter
from news.models import Post

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    url(r'^list/$', object_filter, {'model': Post}),
]
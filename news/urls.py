from django.urls import path
from django_filters import views

from .views import PostList, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView

from django.conf.urls import url
from django_filters.views import object_filter
from news.models import Post


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    # path('<int:pk>', NewsDetail.as_view()),
    url(r'^list/$', object_filter, {'model': Post}),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post_create', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),

]

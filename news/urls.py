from django.urls import path
from .views import PostList  # импортируем наше представление


urlpatterns = [
    path('', PostList.as_view()),
]
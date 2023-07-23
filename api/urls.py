from django.urls import path
from .views import PostsView, PostsDetailView, AuthorsView

app_name = 'api'

urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:post_id>', PostsDetailView.as_view(), name='posts_detail'),
    path('authors/', AuthorsView.as_view(), name='authors'),
]

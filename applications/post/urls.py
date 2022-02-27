from django.urls import path

from applications.post.views import PostListView

urlpatterns = [
    path('post/', PostListView.as_view())
]

from rest_framework import generics

from applications.post.models import Post
from applications.post.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


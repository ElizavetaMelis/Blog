from rest_framework import serializers

from applications.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Post
        fields = '__all__'

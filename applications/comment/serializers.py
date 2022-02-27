from rest_framework import serializers

from applications.comment.models import Answer, Comment


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'author', 'comment', 'title', 'public_date')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        answer = Answer.objects.create(**validated_data)
        return answer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'title', 'public_date')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        comment = Comment.objects.create(**validated_data)
        return comment

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['post'] = instance.post.title
        rep['author'] = instance.author.email
        rep['title'] = AnswerSerializer(Answer.objects.filter(comment=instance.id), many=True).data
        return rep


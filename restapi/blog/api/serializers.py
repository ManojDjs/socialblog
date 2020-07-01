from blog.models import Blogpost,Comment,Messages,Posts
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('post',)

class BlogpostSerializer(serializers.ModelSerializer):
    posts = CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Blogpost
        fields = '__all__'
class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'



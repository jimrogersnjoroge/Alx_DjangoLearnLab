from .models import Post, Comment, Like
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()
#Post Serializer
class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at',
            'author'
        ]
    def validate(self, data):
        if "forbidden_content" in data.get('content', ''):
            raise ValidationError("No forbidden words allowed")   
        
#Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'created_at',
            'updated_at',
            'author',
            'post'
        ]

    def validate(self, data):
        if "forbidden_content" in data.get('content', ''):
            raise ValidationError({"message": "Content contains forbidden words"})

        return data
#Like Serializer
class LikeSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    class Meta:
        model = Like
        fields = [
            'id',
            'created_at',
            'updated_at',
            'author',
            'post'
        ]
    
    #Validation of likes
    def validate(self, data):
        if data['author'] == data['post'].author:
            raise ValidationError({"message": "You cannot like your own post"})
        return data
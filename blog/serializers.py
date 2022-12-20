# Core imports.
from django.contrib.auth import get_user_model

# Third-party imports.
from rest_framework import serializers

from .models import Post, Comment, Category


User = get_user_model()


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

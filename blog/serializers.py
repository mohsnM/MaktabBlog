from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Category, Comment, Post

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

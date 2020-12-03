from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Article
        fields = ('id','title', 'content', 'genre', 'rate', 'user', 'created_at', 'updated_at')
        read_only_fields = ('user', 'created_at', 'updated_at',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','user', 'article', 'content', 'created_at', 'updated_at')
        read_only_fields = ('user', 'article', 'created_at', 'updated_at')
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
import datetime

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication]) # 토큰 유효한지 확인
@permission_classes([IsAuthenticated])  # user authenticated한지 DRF에서 검사한다!!
def article_list_create(request): 
    if request.method=='GET': 
        articles = Article.objects.all()
        serializer= ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    else:
        # new_data = request.data
        # new_data['user'] = request.user.pk
        serializer = ArticleSerializer(data=request.data)
        # print('hello')
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_update_delete(request, article_pk): 
    article = get_object_or_404(Article, pk=article_pk)
    if request.method=='PUT' : 
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data)
    else:
        article.delete()
        # 삭제될 때 삭제된 데이터의 id 값을 보여준다.
        return Response({'id':article_pk})


# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def article_detail(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     serializer = ArticleSerializer(article)
#     return Response(serializer.data)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    print('hello')
    if request.method=='GET':
        comments = article.comments.all()
        serializer= CommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response({'id': comment_pk})



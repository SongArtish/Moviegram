from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')
    if password != passwordConfirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다!!!'})
    
    serializer = UserSerializer(data= request.data)

    if serializer.is_valid(raise_exception=True) : 
        user=serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    serializer= UserSerializer(user)
    return Response(serializer.data)

    
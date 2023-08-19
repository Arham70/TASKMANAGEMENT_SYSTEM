from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from rest_framework.decorators import api_view
from .serializer import CustomUserSerializer


@api_view(['POST'])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_users(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # try:
    #     user = CustomUser.objects.get(email=email)
    #     print(f"email:{email}")
    # except CustomUser.DoesNotExist:
    #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    #
    # if check_password(password, CustomUser.password):
    #     token, created = Token.objects.get_or_create(user=user)
    #     return Response({'token': token.key}, status=status.HTTP_200_OK)
    # else:
    #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    user = CustomUser.objects.get(email=email)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_user(request):
    request.auth.delete()
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

from django.contrib.auth import authenticate, logout
from pizza_lab.accounts.models import CustomUser  # type: ignore
from pizza_lab.accounts.serializers import ShortCustomUserSerializer  # type: ignore
from rest_framework import generics as rest_views
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

class UserListApiView(rest_views.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ShortCustomUserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(is_active=True)

    def get_serializer_context(self):
        return {'request': self.request}


class UserRegisterApiView(rest_views.CreateAPIView):
    serializer_class = ShortCustomUserSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserLoginApiView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({
            'message': 'Logged in successfully',
            'token': access_token})


class UserLogoutApiView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'})


class UserEditApiView(rest_views.UpdateAPIView):
    serializer_class = ShortCustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save()

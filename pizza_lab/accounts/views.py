from pizza_lab.accounts.models import CustomUser  # type: ignore
from pizza_lab.accounts.serializers import ShortCustomUserSerializer  # type: ignore
from rest_framework import generics as rest_views
from rest_framework.permissions import IsAuthenticated


class UserListApiView(rest_views.ListAPIView):
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



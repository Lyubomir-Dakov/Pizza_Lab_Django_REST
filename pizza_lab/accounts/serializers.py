from rest_framework import serializers
from pizza_lab.accounts.models import CustomUser  # type: ignore


class ShortCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'is_staff', 'is_active']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request_user = self.context['request'].user
        if not request_user.is_superuser:
            ret.pop('is_active', None)
            ret.pop('is_staff', None)
        return ret

from rest_framework import serializers
from pizza_lab.accounts.models import CustomUser  # type: ignore


class ShortCustomUserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['email', 'is_staff', 'is_active', 'type']

    @staticmethod
    def get_type(obj):
        type_mapping = {
            'Owners': 'Owner',
            'Clients': 'Client',
            'Managers': 'Manager',
            'Cashiers': 'Cashier',
            'Cookers': 'Cook',
            'Cleaners': 'Cleaner'
        }
        group = obj.groups.first()
        if group:
            return type_mapping.get(group.name, group.name)
        return None

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request_user = self.context['request'].user
        if not request_user.is_superuser:
            ret.pop('is_active', None)
            ret.pop('is_staff', None)
        return ret

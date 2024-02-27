from rest_framework import serializers
from pizza_lab.accounts.models import Employee


class ShortEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

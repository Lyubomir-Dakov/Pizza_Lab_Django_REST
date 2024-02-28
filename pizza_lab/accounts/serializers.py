from rest_framework import serializers
from pizza_lab.accounts.models import Employee  # type: ignore

from pizza_lab.restaurants.serializers import ShortRestaurantSerializer


class ShortEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DemoSerializer(serializers.Serializer):
    employees = ShortEmployeeSerializer(many=True)
    employees_count = serializers.IntegerField()
    restaurants = ShortRestaurantSerializer(many=True)
    first_restaurant = serializers.CharField()

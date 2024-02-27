from pizza_lab.accounts.models import Employee  # type: ignore
from pizza_lab.accounts.serializers import ShortEmployeeSerializer  # type: ignore
from pizza_lab.restaurants.serializers import ShortRestaurantSerializer  # type: ignore
from rest_framework import generics as rest_views
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    restaurant = ShortRestaurantSerializer()

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeesListApiView(rest_views.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

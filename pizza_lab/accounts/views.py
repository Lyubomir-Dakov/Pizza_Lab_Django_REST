from pizza_lab.accounts.models import Employee  # type: ignore
from pizza_lab.accounts.serializers import ShortEmployeeSerializer  # type: ignore
from pizza_lab.restaurants.serializers import ShortRestaurantSerializer  # type: ignore
from rest_framework import generics as rest_views
from rest_framework import serializers
from rest_framework import views as rest_base_views
from rest_framework.response import Response

from pizza_lab.restaurants.models import Restaurant

from pizza_lab.accounts.serializers import DemoSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    restaurant = ShortRestaurantSerializer()

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeesListApiView(rest_views.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DemoApiView(rest_base_views.APIView):

    def get(self, request):
        employees = Employee.objects.all()
        restaurants = Restaurant.objects.all()

        body = {
            "employees": employees,
            "employees_count": employees.count(),
            "restaurants": restaurants,
            "first_restaurant": restaurants.first(),
        }

        serializer = DemoSerializer(body)

        return Response(serializer.data)

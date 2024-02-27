from pizza_lab.accounts.views import ShortEmployeeSerializer  # type: ignore
from pizza_lab.restaurants.models import Restaurant  # type: ignore
from rest_framework import generics as rest_views
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    employees = ShortEmployeeSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = "__all__"


# Create your views here.
class RestaurantListApiView(rest_views.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
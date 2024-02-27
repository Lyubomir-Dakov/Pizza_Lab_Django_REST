from django.urls import path

from pizza_lab.restaurants.views import RestaurantListApiView  # type: ignore

urlpatterns = [
    path("", RestaurantListApiView.as_view(), name="restaurants")
]

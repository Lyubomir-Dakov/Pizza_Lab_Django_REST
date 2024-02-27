from django.contrib import admin
from pizza_lab.restaurants.models import Restaurant  # type: ignore


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

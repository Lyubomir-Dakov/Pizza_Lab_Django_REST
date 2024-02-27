from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("pizza_lab.accounts.urls")),
    path("restaurants/", include("pizza_lab.restaurants.urls"))
]

from django.urls import path

from pizza_lab.accounts.views import UserListApiView  # type: ignore

urlpatterns = [
    path("", UserListApiView.as_view(), name="users api list"),
]

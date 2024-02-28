from django.urls import path

from pizza_lab.accounts.views import EmployeesListApiView  # type: ignore

from pizza_lab.accounts.views import DemoApiView

urlpatterns = [
    path("employees/", EmployeesListApiView.as_view(), name="api list employees"),
    path("details/", DemoApiView.as_view(), name="details")
]

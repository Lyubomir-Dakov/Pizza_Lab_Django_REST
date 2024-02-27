from django.urls import path

from pizza_lab.accounts.views import EmployeesListApiView  # type: ignore

urlpatterns = [
    path("employees/", EmployeesListApiView.as_view(), name="api list employees")
]

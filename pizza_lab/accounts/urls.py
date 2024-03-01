from django.urls import path

from pizza_lab.accounts.views import UserListApiView, UserRegisterApiView, UserLoginApiView, UserLogoutApiView, UserEditApiView  # type: ignore

urlpatterns = [
    path('register/', UserRegisterApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('edit/', UserEditApiView.as_view(), name='user edit'),
    path('accounts/', UserListApiView.as_view(), name='users list'),
]

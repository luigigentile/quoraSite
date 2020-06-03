from django.urls import path

from users.api.views import CurrentUserAPIView
from users.api.views import UsersAPIView

urlpatterns = [
    path('user/', CurrentUserAPIView.as_view(), name = 'current-user'),
    path('users/', UsersAPIView.as_view(), name = 'users')

]

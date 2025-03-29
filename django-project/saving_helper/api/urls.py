from django.urls import path
from .views import get_user, create_user, user_detail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

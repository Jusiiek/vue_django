from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserListView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('user_list/', UserListView.as_view(), name='user-list'),
]

urlpatterns += router.urls

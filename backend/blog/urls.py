from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, RegisterView

router=DefaultRouter()

router.register('posts', PostViewSet, basename='post' )

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
]+ router.urls

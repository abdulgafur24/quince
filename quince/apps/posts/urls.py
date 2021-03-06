from django.urls import path, include

from . import views


from .views import PostViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.PostsView.as_view(), name="index"),
]

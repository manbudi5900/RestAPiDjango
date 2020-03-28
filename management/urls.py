from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DosenViewSet, MatkulViewSet
router = DefaultRouter()
router.register(r'dosen', DosenViewSet)
router.register(r'matakuliah', MatkulViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DosenViewSet, MatkulViewSet, MahasiswaViewSet, MengikutiViewSet
router = DefaultRouter()
router.register(r'dosen', DosenViewSet)
router.register(r'matakuliah', MatkulViewSet)
router.register(r'mahasiswa', MahasiswaViewSet)
router.register(r'mengikuti', MengikutiViewSet, basename='mengikuti')
# router.register(r'rawSQL', SQLRAWQUERY)

urlpatterns = [
    path('', include(router.urls)),
    # path(),
]


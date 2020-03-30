from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from .models import Dosen, Matkul, Mahasiswa, Mengikuti
from .serializers import DosenSerializer, MatkulSerializer, MahasiswaSerializer, MengikutiSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from rest_framework import permissions
from management.permissions import IsOwnerOrReadOnly
from rest_framework.renderers import JSONRenderer


class DosenViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    queryset = Dosen.objects.all()
    serializer_class = DosenSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('name', 'nip')
    search_fields = ['name']
    ordering = ('name')

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(DosenViewSet, self).get_serializer(*args, **kwargs)


class MatkulViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Matkul.objects.all()
    serializer_class = MatkulSerializer
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(MatkulViewSet, self).get_serializer(*args, **kwargs)

class MahasiswaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer]
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(MahasiswaViewSet, self).get_serializer(*args, **kwargs)

class MengikutiViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Mengikuti.objects.all()
    serializer_class = MengikutiSerializer
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(MengikutiViewSet, self).get_serializer(*args, **kwargs)

# class MengikutiViewSet(APIView):

#     def post(self, request, *args, **kwargs):
#         nim = request.data['nim']
#         kode_matkul = request.data['kode_matkul']
#         serializer = GetProductSerializer(Mengikuti.objects.filter(nim=nim, kode_matkul=kode_matkul).prefetch_related('nim','kode_matkul'), many=True)
#         return Response(serializer.data)
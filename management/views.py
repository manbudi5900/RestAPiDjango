from rest_framework import status, viewsets, generics
from .models import Dosen, Matkul
from .serializers import DosenSerializer, MatkulSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class DosenViewSet(viewsets.ModelViewSet):
    queryset = Dosen.objects.all()
    serializer_class = DosenSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('name', 'nip')
    search_fields = ['name']
    ordering = ('name',)

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(DosenViewSet, self).get_serializer(*args, **kwargs)


class MatkulViewSet(viewsets.ModelViewSet):
    queryset = Matkul.objects.all()
    serializer_class = MatkulSerializer
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            if isinstance(data, list):
                kwargs["many"] = True
        return super(MatkulViewSet, self).get_serializer(*args, **kwargs)
    
# class GithubUserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = GithubUser.objects.all()
#     serializer_class = GithubUserSerializer



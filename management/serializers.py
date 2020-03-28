from rest_framework import serializers
from .models import *


class DosenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dosen
        fields = '__all__'


class MatkulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matkul
        fields = '__all__'

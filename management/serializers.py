from rest_framework import serializers
from .models import *



class DosenSerializer(serializers.ModelSerializer):
    matkul = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Dosen
        fields = ['nip', 'name', 'phone', 'nip','alamat', 'flag', 'matkul']


class MatkulSerializer(serializers.ModelSerializer):
    mengikuti = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Matkul
        fields = ['kode_matkul', 'nama_matkul', 'sks', 'nip', 'mengikuti']

class MengikutiSerializer(serializers.ModelSerializer):
    #  = serializers.RelatedField(read_only=True, many=True)
    class Meta:
        model = Mengikuti
        fields = ['kode_matkul']

class MahasiswaSerializer(serializers.ModelSerializer):
    mengikuti = MengikutiSerializer(read_only=True, many=True)
    class Meta:
        model = Mahasiswa
        fields = ['nim', 'nama', 'alamat','mengikuti']





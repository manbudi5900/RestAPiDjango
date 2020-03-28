from django.db import models


class Dosen(models.Model):
    nip= models.CharField(primary_key=True, max_length=20, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=12, null=True, blank=False )
    alamat = models.CharField(max_length=100, null=True, blank=False)
    flag = models.FileField(upload_to='static/images/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.nip


class Matkul(models.Model):
    kode_matkul = models.CharField(primary_key=True, max_length=50, null=False, blank=False)
    nama_matkul = models.CharField(max_length=255, null=False, blank=False)
    sks = models.IntegerField(default=0, verbose_name='The number of Repositories')
    nip = models.ForeignKey('Dosen',to_field='nip', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s (%s)" % (self.kode_matkul)

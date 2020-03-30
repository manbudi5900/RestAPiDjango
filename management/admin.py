from django.contrib import admin
from .models import Dosen, Matkul, Mahasiswa, Mengikuti

admin.site.register(Dosen)
admin.site.register(Matkul)
admin.site.register(Mahasiswa)
admin.site.register(Mengikuti)


from django.conf.urls import url, include 
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('management.urls')),

    # url(r'^', include('management.urls')),
]
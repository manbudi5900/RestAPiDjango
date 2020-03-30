from django.conf.urls import url, include 
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('management.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # url(r'^', include('management.urls')),
]
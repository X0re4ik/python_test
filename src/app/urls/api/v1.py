from django.contrib import admin
from django.urls import include, path, re_path
from mp4.urls import urlpatterns
__API_VERSION__ = 1
__ROOT_API_PATH__ = f"v{__API_VERSION__}/"

urlpatterns = [
    re_path(r'^mp4/', include("mp4.urls")),
    *urlpatterns,           
]
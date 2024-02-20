from django.contrib import admin
from django.urls import include, path, re_path
from mv4.urls import urlpatterns
__API_VERSION__ = 1
__ROOT_API_PATH__ = f"v{__API_VERSION__}/"

urlpatterns = [
    re_path(r'^mv4/', include("mv4.urls")),
    *urlpatterns,           
]
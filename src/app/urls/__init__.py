from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("app.urls.api.v1")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
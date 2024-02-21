from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

from mp4.api.views import MP4ViewSet

router = DefaultRouter()
router.register("file", MP4ViewSet, "file")

urlpatterns = router.urls
from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

from mv4.api.views import MV4ViewSet

router = DefaultRouter()
router.register("file", MV4ViewSet, "file")

urlpatterns = router.urls
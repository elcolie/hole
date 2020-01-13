from rest_framework import routers

from hole.users.api.viewsets import UserViewSet

app_name = "apis"

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls

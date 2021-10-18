from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()
router.register('', UserViewSet, basename='profiles')
urlpatterns = router.urls

from .views import ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ReviewViewSet, basename='reviews')
urlpatterns = router.urls

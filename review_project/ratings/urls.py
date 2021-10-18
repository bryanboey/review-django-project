from .views import StarRatingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('star', StarRatingViewSet, basename='star-rating')
router.register('price', StarRatingViewSet, basename='price-rating')
urlpatterns = router.urls

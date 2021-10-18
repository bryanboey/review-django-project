from .views import EstablishmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', EstablishmentViewSet, basename='establishments')
urlpatterns = router.urls

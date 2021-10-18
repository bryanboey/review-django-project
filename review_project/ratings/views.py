from .models import StarRating, PriceRating
from .serializers import StarRatingSerializer, PriceRatingSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


# StarRatingViewSet
class StarRatingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StarRatingSerializer
    queryset = StarRating.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


# PriceRatingViewSet
class PriceRatingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PriceRatingSerializer
    queryset = PriceRating.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

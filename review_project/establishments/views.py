from .models import Establishment
from .serializers import EstablishmentSerializer, EstablishmentDetailSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Avg, F


# ModelViewSet
class EstablishmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EstablishmentSerializer
    queryset = Establishment.objects.annotate(
        avg_star_rating=Avg('star_ratings__rating'),
        total_star_votes=Count('star_ratings', distinct=True),
        avg_price_rating=Avg('price_ratings__rating'),
        total_price_votes=Count('price_ratings', distinct=True),
        review_count=Count('reviews', distinct=True),
    ).order_by(
        F('avg_star_rating').desc(nulls_last=True)
    )
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    # in the future add category/tags in search fields
    search_fields = ['name', 'address']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EstablishmentDetailSerializer(instance)
        return Response(serializer.data)

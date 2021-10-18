from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


# ReviewViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    # in the future add category in search fields
    search_fields = ['establishment__name']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

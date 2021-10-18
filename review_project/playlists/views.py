from .models import Playlist
from establishments.models import Establishment
from .serializers import PlaylistSerializer, PlaylistDetailSerializer, EstablishmentPlaylistSerializer
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# ModelViewSet
class PlaylistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlaylistSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Playlist.objects.filter(owner=self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PlaylistDetailSerializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PlaylistAddView(generics.ListCreateAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        playlist = Playlist.objects.get(id=data['playlist_id'])
        establishment = Establishment.objects.get(id=data['establishment_id'])
        playlist.establishment.add(establishment)

        playlist.save()

        serializer = PlaylistSerializer(playlist)

        return Response(serializer.data)


class PlaylistRemoveView(generics.ListCreateAPIView):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        playlist = Playlist.objects.get(id=data['playlist_id'])
        establishment = Establishment.objects.get(id=data['establishment_id'])
        playlist.establishment.remove(establishment)

        playlist.save()

        serializer = PlaylistSerializer(playlist)

        return Response(serializer.data)



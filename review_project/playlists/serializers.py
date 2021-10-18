from .models import Playlist
from rest_framework import serializers
from establishments.models import Establishment
from establishments.serializers import EstablishmentSerializer


class PlaylistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Playlist
        fields = ['id', 'owner', 'name']


class EstablishmentPlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ['id']


class PlaylistDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    establishment = EstablishmentSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'owner', 'name', 'establishment', 'created']
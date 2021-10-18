from rest_framework import serializers
from .models import StarRating, PriceRating
from establishments.models import Establishment


class StarRatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    establishment = serializers.ReadOnlyField(source='establishment.name')
    establishment_id = serializers.PrimaryKeyRelatedField(
        queryset=Establishment.objects.all(), write_only=True
    )

    class Meta:
        model = StarRating
        fields = ['establishment_id', 'establishment', 'rating', 'user']

    def create(self, validated_data):
        establishment = validated_data.pop('establishment_id')
        rating = StarRating.objects.create(
            establishment=establishment, **validated_data
        )
        return rating


class PriceRatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    establishment = serializers.ReadOnlyField(source='establishment.name')
    establishment_id = serializers.PrimaryKeyRelatedField(
        queryset=Establishment.objects.all(), write_only=True
    )

    class Meta:
        model = PriceRating
        fields = ['establishment_id', 'establishment', 'rating', 'user']

    def create(self, validated_data):
        establishment = validated_data.pop('establishment_id')
        rating = PriceRating.objects.create(
            establishment=establishment, **validated_data
        )
        return rating

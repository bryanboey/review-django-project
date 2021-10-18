from .models import Establishment
from rest_framework import serializers
from reviews.models import Review
from django.contrib.auth.models import User


class EstablishmentSerializer(serializers.ModelSerializer):
    avg_star_rating = serializers.FloatField(read_only=True)
    total_star_votes = serializers.IntegerField(read_only=True)
    avg_price_rating = serializers.FloatField(read_only=True)
    total_price_votes = serializers.IntegerField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Establishment
        fields = [
            'id', 'name', 'address', 'created', 'avg_star_rating',
            'total_star_votes', 'avg_price_rating', 'total_price_votes', 'review_count'
        ]


class ReviewEstablishmentSerializer(serializers.ModelSerializer):
    written_by = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = [
            'id', 'written_by', 'title', 'body', 'created', 'updated'
        ]


class EstablishmentDetailSerializer(serializers.ModelSerializer):
    avg_star_rating = serializers.FloatField()
    total_star_votes = serializers.IntegerField()
    avg_price_rating = serializers.FloatField()
    total_price_votes = serializers.IntegerField()
    reviews = ReviewEstablishmentSerializer(many=True, read_only=True)

    class Meta:
        model = Establishment
        fields = [
            'id', 'name', 'address', 'created', 'avg_star_rating',
            'total_star_votes', 'avg_price_rating', 'total_price_votes', 'reviews'
        ]

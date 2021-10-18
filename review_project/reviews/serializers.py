from rest_framework import serializers
from .models import Review
from establishments.models import Establishment


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    establishment_id = serializers.PrimaryKeyRelatedField(
        queryset=Establishment.objects.all(), write_only=True
    )

    class Meta:
        model = Review
        fields = [
            'establishment_id', 'id', 'user', 'establishment',
            'title', 'body', 'created', 'updated'
        ]
        depth = 1

    def create(self, validated_data):
        establishment = validated_data.pop('establishment_id')
        review = Review.objects.create(
            establishment=establishment, **validated_data
        )
        return review

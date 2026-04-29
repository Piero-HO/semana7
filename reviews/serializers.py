from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'id',
            'movie',
            'author_name',
            'rating',
            'spoiler_text'
        ]
from rest_framework import serializers
from movies.models import Movie
from .review_serializer import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "runtime_formatted",
            "release_date",
            "reviews",
            "avg_rating",
        )

    def get_runtime_formatted(self, obj):
        hours, minutes = divmod(obj.runtime, 60)
        return f"{hours}:{minutes:02}"

    def get_avg_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0
from rest_framework import serializers
from apiApp.models import Watchlist, StreamPlatform, Review


# Model Serializer
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude=('watchlist',)
class WatchListSerializer(serializers.ModelSerializer):
    platform =  serializers.CharField(source='platform.name')
    class Meta:
        model = Watchlist
        fields='__all__'
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
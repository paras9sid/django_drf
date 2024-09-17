from rest_framework import serializers
from apiApp.models import Movie
# from apiApp.models import Watchlist, StreamPlatform, Review


# class ReviewSerializer(serializers.ModelSerializer):
#     review_user = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = Review
#         # fields= '__all__'
#         exclude=['watchlist']

# #model serializer
# class WatchListSerializer(serializers.ModelSerializer):
    
#     reviews = ReviewSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Watchlist
#         fields='__all__'
#         # fields = ('id', 'name', 'description')
#         # fields = ['id', 'name', 'description']
#         # exclude=['active','name']
        
# class StreamPlatformSerializer(serializers.ModelSerializer):
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    #realtionship
    # watchlist = WatchListSerializer(many=True, read_only=True)
    
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='watch_list_detail'
    # )

    
    # class Meta:
    #     model = StreamPlatform
    #     fields = '__all__'
        # extra_kwargs = {
        #     'url': {'view_name': 'watch_list_detail'}, 
        # }



class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    
    # Field-level Validation
    def validate_name(self, value):        
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short.Please write name with more alphabets.")
        return value
        
    # Object Level Validation    
    def validate(self, data):
        if data['name'] ==  data['description']:
            raise serializers.ValidationError("Title and description should not be same.")
        return data        
    
    

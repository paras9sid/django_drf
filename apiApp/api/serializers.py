from rest_framework import serializers
# from apiApp.models import Movie
from apiApp.models import Watchlist, StreamPlatform, Review


# Model Serializer

class ReviewSerializer(serializers.ModelSerializer):
    # review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields= '__all__'
        # exclude=['watchlist']
        
class WatchListSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)    
    class Meta:
        model = Watchlist
        fields='__all__'
        # fields = ('id', 'name', 'description')
        # exclude=['active','name']
        
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    # Nested Serializer Realtionship
    
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='watch_list_detail'
    # )

    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        # serializers.HyperlinkedModelSerializer - nelow extra field awith code required.
        extra_kwargs = {
            'url': {'view_name': 'watch_list_detail'}, 
        }






# ----------------------------------------------

# Model Serializer

# class MovieSerializer(serializers.ModelSerializer):
    
    # Custom Serializer Fields
    # len_name = serializers.SerializerMethodField()
    # class Meta:
        # model = Movie
        # fields = '__all__'
        # fields = ['id','name','description']
        # exclude = ['active'] # only this field not wanted so exclude cvariable defined with value not to be seen
        
    # Custom Serializer Method
    # def get_len_name(self, obj):
        # length = len(obj.name)
        # return length
        
    # Field-level Validation
    # def validate_name(self, value):        
        # if len(value) < 3:
        #     raise serializers.ValidationError("Name is too short.Please write name with more alphabets.Field-Level Validation")
        # return value
        
            
    # Object Level Validation    
    # def validate(self, data):
        # if data['name'] ==  data['description']:
        #     raise serializers.ValidationError("Title and description should not be same.")
        # return data        
    


# -----------------------------------------------------------------------------------


# Validator
# def name_length(value):
    # if len(value) < 3:
    #         raise serializers.ValidationError("Name is too short.Validator function method implemented.")
    # return value
            

# class MovieSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(validators=[name_length])
    # description = serializers.CharField()
    # active = serializers.BooleanField()
    
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    
    
    # Field-level Validation
    # def validate_name(self, value):        
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name is too short.Please write name with more alphabets.Field-Level Validation")
    #     return value
        
            
    # Object Level Validation    
    # def validate(self, data):
    #     if data['name'] ==  data['description']:
    #         raise serializers.ValidationError("Title and description should not be same.")
    #     return data        
    
    

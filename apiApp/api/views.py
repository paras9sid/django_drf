from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status , generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import  IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle

from . import serializers , throttling , permissions
from apiApp.models import Watchlist, StreamPlatform, Review

class UserReview(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer

    # filtering against query params
    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Review.objects.filter(review_user__username=username) # watchlistmodel field from model Review
class ReviewCreate(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [throttling.ReviewCreateThrottle]

    # AssertionError at /watch/1/review-create/
    # 'ReviewCreate' should either include a `queryset` attribute, or override the `get_queryset()` method.
    def get_queryset(self):
        return Review.objects.all()
    
    #over write create method
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)
        
        #  1 user 1 review/movie not more
        review_user = self.request.user
        review_queryset= Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")
        
        if watchlist.number_of_ratings == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2
            
        watchlist.number_of_ratings += 1
        watchlist.save()        
        serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewList(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [throttling.ReviewListThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']

    # customizing url for displaying review for 1 movie at a time
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk) # watchlistmodel field from model Review
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
class WatchListAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self, request):
        watchlist = Watchlist.objects.all()
        serializer = serializers.WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = serializers.WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListDetailAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self,request,pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
            serializer = serializers.WatchListSerializer(watchlist)
            return Response(serializer.data)
        except Watchlist.DoesNotExist:
            return Response({'Error':'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        watchlist = Watchlist.objects.get(pk=pk)
        serializer = serializers.WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        watchlist = Watchlist.objects.get(pk=pk)
        watchlist.delete()       
        return Response(status=status.HTTP_204_NO_CONTENT)

# Model Viewset
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = serializers.StreamPlatformSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


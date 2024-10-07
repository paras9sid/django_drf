from django.shortcuts import get_object_or_404

from apiApp.models import Watchlist, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .throttling import ReviewCreateThrottle, ReviewListThrottle


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework import mixins

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle


class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # throttle_classes = [ReviewListThrottle, AnonRateThrottle]

    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username) # watchlistmodel field from model Review
    
    # filtering against query params
    def get_queryset(self):

        username = self.request.query_params.get('username')
        # if username is not None:
        #     queryset = queryset.filter(purchaser__username=username)
        # return queryset
    
        # username = self.kwargs['username']
        return Review.objects.filter(review_user__username=username) # watchlistmodel field from model Review


class ReviewCreate(generics.CreateAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]


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
    
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]

    # customizing url for displaying review for 1 movie at a time
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk) # watchlistmodel field from model Review
        
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'



class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        watchlist = Watchlist.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchListDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly]

    def get(self,request,pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
            serializer = WatchListSerializer(watchlist)
            return Response(serializer.data)
        except Watchlist.DoesNotExist:
            return Response({'Error':'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        watchlist = Watchlist.objects.get(pk=pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        watchlist = Watchlist.objects.get(pk=pk)
        watchlist.delete()       
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamPlatformAV(APIView):

    permission_classes = [IsAdminOrReadOnly]

    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True,  context={'request': request})
        return Response(serializer.data)

    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):

    permission_classes = [IsAdminOrReadOnly] 

    def get(self,request,pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)            
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self,request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()       
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Model Viewset
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]


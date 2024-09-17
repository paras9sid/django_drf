from django.shortcuts import get_object_or_404

# from apiApp.models import Movie
# from .serializers import MovieSerializer

from apiApp.models import Watchlist, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import generics
# # from rest_framework import mixins

# from rest_framework import viewsets
# from rest_framework.exceptions import ValidationError
# from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

# from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly




# class ReviewCreate(generics.CreateAPIView):
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Review.objects.all()
    
#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         watchlist = Watchlist.objects.get(pk=pk)
        
#         #  1 user 1 review/movie not more
#         review_user = self.request.user
#         review_queryset= Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
#         if review_queryset.exists():
#             raise ValidationError("You have already reviewed this movie.")
        
#         if watchlist.number_of_ratings == 0:
#             watchlist.avg_rating = serializer.validated_data['rating']
#         else:
#             watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
            
#         watchlist.number_of_ratings += 1
#         watchlist.save()
        
#         serializer.save(watchlist=watchlist, review_user=review_user)
#         # return super().perform_create(serializer)

# class ReviewList(generics.ListAPIView):
#     # queryset = Review.objects.all() # accessing all reviews
    
#     serializer_class = ReviewSerializer
#     # permission_classes = [IsAuthenticated]
    
#     #customizing url 
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Review.objects.filter(watchlist=pk) # watchlistmodel field from model Review
    
# # class ReadOnly(BasePermission):
# #     def has_permission(self, request, view):
# #         return request.method in SAFE_METHODS
    
# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # permission_classes = [IsAuthenticated|ReadOnly]
#     # permission_classes = [IsAdminOrReadOnly]
#     permission_classes = [IsReviewUserOrReadOnly]



# class ReviewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)




class WatchListAV(APIView):
    
#     permission_classes = [IsAdminOrReadOnly]
    
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
    
#     permission_classes = [IsAdminOrReadOnly]
    
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
    
    # permission_classes = [IsAdminOrReadOnly]

    def get(self,request):
        platform = StreamPlatform.objects.all()
        # serializer = StreamPlatformSerializer(platform, many=True,  context={'request': request})
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailAV(APIView):
    
    # permission_classes = [IsAdminOrReadOnly] 
    
    def get(self,request,pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie)
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()       
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

        
        
# # # Model Viewset
# class StreamPlatformVS(viewsets.ModelViewSet):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
#     permission_classes = [IsAdminOrReadOnly]


# #for read only 
# class StreamPlatformVS(viewsets.ReadOnlyModelViewSet):
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
        
# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist, context={'request': request})
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    



#  ------------------------------------

# class MovieListAV(APIView):
    
# #     permission_classes = [IsAdminOrReadOnly]
    
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
# class MovieDetailAV(APIView):
    
# #     permission_classes = [IsAdminOrReadOnly]
    
#     def get(self,request,pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)
        
#     def put(self,request,pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()       
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
        
        
        

#  --------------------------------------------------------------------------------------------
# FBV


# @api_view(['GET','POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request,pk):
    
#     if request.method=='GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)
        
#     if request.method=='PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method=='DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()       
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

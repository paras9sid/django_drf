
from django.urls import path, include
# from .views import movie_list, movie_details
# from .views import MovieListAV,MovieDetailAV
# from . views import (WatchListAV, WatchListDetailAV, StreamPlatformAV, 
#                     StreamPlatformDetailAV,ReviewList, ReviewDetail, 
#                     ReviewCreate, StreamPlatformVS)

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('stream',StreamPlatformVS,basename='streamplatform')
# # urlpatterns = router.urls



urlpatterns = [
    # path('list/',movie_list,name='movie_list'),
    # path('list/<int:pk>/',movie_details,name='movie_detail'),
    
    # path('list/',MovieListAV.as_view()),
    # path('list/<int:pk>/',MovieDetailAV.as_view()),
    
    # path('list/',WatchListAV.as_view(),name='watch_list'),
    # path('list/<int:pk>/',WatchListDetailAV.as_view(),name='watch_list_detail'),
    
    # path('',include(router.urls)),
    
    # path('stream/',StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name='stream_detail'),
    
    # path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review_create'),
    # path('<int:pk>/reviews/',ReviewList.as_view(),name='review_list'),
    # path('reviews/<int:pk>/',ReviewDetail.as_view(),name='review_detail'),
    
    # path('review/',ReviewList.as_view(),name='review_list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name='review_detail'),

]

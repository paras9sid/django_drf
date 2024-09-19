from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . views import (WatchListAV, WatchListDetailAV,
                    ReviewList,ReviewDetail,ReviewCreate,
                    StreamPlatformVS)


# viewsets and routers
router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')
# urlpatterns = router.urls



urlpatterns = [
    
    path('list/',WatchListAV.as_view(),name='watch_list'),
    path('list/<int:pk>/',WatchListDetailAV.as_view(),name='watch_list_detail'),
    
    # path('stream/',StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name='stream_detail'),
    
    # path('review/',ReviewList.as_view(),name='review_list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name='review_detail'),

    # viewsetts and routers
    path('',include(router.urls)),
    
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review_list'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review_detail'),
    
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review_create'),


]

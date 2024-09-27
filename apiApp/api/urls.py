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
    
    path('list/',WatchListAV.as_view(),name='watch-list'),
    path('<int:pk>/',WatchListDetailAV.as_view(),name='watchlist-detail'),

    # viewsetts and routers
    path('',include(router.urls)),
    
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
    
]

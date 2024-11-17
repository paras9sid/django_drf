from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

# viewsets and routers
router = DefaultRouter()
router.register('stream',views.StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    
    path('list/',views.WatchListAV.as_view(),name='watch-list'),
    path('<int:pk>/',views.WatchListDetailAV.as_view(),name='watchlist-detail'),

    # viewsetts and routers
    path('',include(router.urls)),

    path('<int:pk>/reviews/create/',views.ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',views.ReviewList.as_view(),name='review-list'),
    path('reviews/<int:pk>/',views.ReviewDetail.as_view(),name='review-detail'),

    # filtering with query params
    path('user-reviews/',views.UserReview.as_view(),name='user-review-detail'),

]

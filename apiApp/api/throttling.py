from rest_framework.throttling import UserRateThrottle



# settings for logged in user onyl
class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'

class ReviewListThrottle(UserRateThrottle):
    scope = 'review-list'
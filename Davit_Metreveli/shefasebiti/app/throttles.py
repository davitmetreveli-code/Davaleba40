from rest_framework.throttling import UserRateThrottle

class CustomPostThrottle(UserRateThrottle):
    scope = 'custom'
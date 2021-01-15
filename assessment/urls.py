from django.contrib import admin
from django.urls import path, include
from aggregator.views import SubscriptionViewSet, ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('subscription', SubscriptionViewSet, basename='Subscription')
router.register('item', ItemViewSet, basename='Item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include(router.urls)),
]

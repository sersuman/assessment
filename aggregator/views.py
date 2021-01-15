from django.shortcuts import render
from rest_flex_fields import (
    FlexFieldsModelViewSet,
    is_expanded,
)
from rest_framework import viewsets
from .serializers import SubscriptionSerializer, ItemSerializer
from .models import Subscription, Item
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Count

class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Subscription.objects.filter(user=user)
        return queryset
    
class ItemViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        topic = Subscription.objects.filter(user=user).values_list('topic')
        queryset = Item.objects.filter(topic__in=topic).annotate(Count('topic'))
        return queryset

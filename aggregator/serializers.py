from .models import Subscription, Item
from rest_framework import serializers
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_flex_fields import FlexFieldsModelSerializer


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('topic',)
        read_only_fields = ['user']
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('__all__')
        
from .models import Notification
from rest_framework import serializers

#Notification Model serializer
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'recipient',
            'actor',
            'verb',
            'target',
            'timestamp',
        ]

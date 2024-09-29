from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions, authentication
from .serializers import NotificationSerializer
from .models import Notification, Post

# Create your views here.

#View for Notifications
class NotificationView(generics.GenericAPIView):
    serializer_class = NotificationSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(recepient=self.request.user)
        notifications.update(is_unread=False)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        action = request.data.get('action')
        post_id= self.request.data.get('post')

        #Validation
        if action == 'like' or action == 'comment' or action == 'follow':
            post = get_object_or_404(Post, id=post_id)
            Notification.objects.create(
                sender=self.request.user,
                recepient=post.author,
                action=action,
                post=post
            )
            return Response({'message': 'Notification sent'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)



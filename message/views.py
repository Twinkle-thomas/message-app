from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from message.models import Message
from message.serializers import MessageSerializer


# Create your views here.
@api_view(['POST'])
def send_message(request):
    sender = request.data.get('sender')
    receiver = request.data.get('receiver')
    content = request.data.get('content')
    chat_room = request.data.get('chat_room')
    message_serializer = MessageSerializer(data=request.data)
    if message_serializer.is_valid():
        message_serializer.save()
        return Response({'message': 'Message sent successfully'},
                        status=status.HTTP_201_CREATED)


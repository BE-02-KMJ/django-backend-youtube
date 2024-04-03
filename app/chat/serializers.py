from rest_framework.serializers import ModelSerializer
from .models import ChatRoom, ChatRoomConnector, ChatMessage

class ChatRoomSerializer(ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"

class MessageSerializer(ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
        read_only_fields = ['sender', 'chatroom']
        depth = 1 

class ConnectorSerializer(ModelSerializer):
    class Meta:
        model = ChatRoomConnector
        fields = '__all__'
        depth = 1

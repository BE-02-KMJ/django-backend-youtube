from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatRoom, ChatMessage
from .serializers import ChatRoomSerializer, ChatMessageSerializer

# html 연결
def chat_html(request):
    return render(request, 'chat.html')

# Create your views here.
# Chat Room
# - Chat Room List
# api/v1/chat/
    # [GET]: 전체 채팅방 조회
    # [POST]: 채팅방 생성
class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        serializer = ChatRoomSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# - chat Room Detail
# api/v1/chat/{room_id}
    # [PUT]: 채팅방 관련 수정
    # [DELETE]: 해당 채팅방 삭제

# Chat Message
# - Chat Message List
# api/v1/chat/{room_id}/messages
    # [GET]: 채팅방 내역 조회
    # [POST]: 채팅방 메세지 생성
class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)    # room : django object
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, room_id):
        user_data = request.data
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        serializer = ChatRoomSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save(room=chatroom, sender=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

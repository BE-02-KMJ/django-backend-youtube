from django.urls import path
from .views import ChatRoomList, ChatMessageList, ChatRoomDetail, chat_html

# api/v1/chat
urlpatterns=[
    path('room/', ChatRoomList.as_view(), name='room-list'),
    path('<int:room_id>/messages', ChatMessageList.as_view(), name='message-list'),
    path("<int:room_id>", ChatRoomDetail.as_view(), name='chatroom-detail'),
    path('chatting', chat_html, name='chatting') 
]

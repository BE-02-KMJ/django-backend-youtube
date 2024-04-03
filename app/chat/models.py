from django.db import models
from users.models import User
from common.models import CommonModel

# Create your models here.
# chatRoom model 분리시 이점
# 1. 관리 용이
# 2. 확장 용이 (오픈채팅방, 업무채팅방 등)
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)
    member = models.ManyToManyField(User, through='ChatRoomConnector')

class ChatRoomConnector(CommonModel):   # 추가
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

class ChatMessage(CommonModel):
    # 정보 통신법 3개월 채팅 보관
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # 알 수 없음.
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

# User:Msg(FK) → 1:N
    # - User: Msg, Msg, Msg → 가능
    # - Msg: User1, User2, User3 → 불가능

# Room:Message (1:N)
    # - Room : Msg, Msg, Msg → 가능
    # - Message : Room1, Room2, Room3 → 불가능
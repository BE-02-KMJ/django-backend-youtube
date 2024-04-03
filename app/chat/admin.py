from django.contrib import admin
from .models import ChatRoom, ChatRoomConnector, ChatMessage

# Register your models here.
@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            '채팅방',
            {
                'fields': ('room_name',)
            },
        ),
    )

    # 표에서 보이는 정보
    list_display = (
        'id','room_name'
    )
    search_fields = ('room_name',)
    ordering = ('created_at',)

@admin.register(ChatRoomConnector)  # 추가
class ConnectorAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            '채팅방',
            {
                'fields': ('chatroom','user')
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'user',
                    'chatroom',
                    ),
            }
        ),
    )
    # 표에서 보이는 정보
    list_display = (
        'chatroom','user'
    )

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            '채팅기록',
            {
                'fields': ('sender','message','chatroom')
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'sender',
                    'message',
                    'chatroom',
                    ),
            }
        ),
    )
    # 표에서 보이는 정보
    list_display = (
        'chatroom','sender','message'
    )

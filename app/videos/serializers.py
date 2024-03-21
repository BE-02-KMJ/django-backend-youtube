from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):
    # Video:User - Video(FK) → User
    user = UserSerializer(read_only=True)
    class Meta:
        model = Video
        fields = '__all__'

class VideoDetailSerializer(serializers.ModelSerializer):
    # Video:User - Video(FK) → User
    user = UserSerializer(read_only=True)

    # Video:Comment - Video → Comment(FK)
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = '__all__'
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

# Create your views here.
# Video와 관련된 REST API

# 1. VideoList
# api/v1/video
# [GET] - 전체 비디오 목록 조회
# [POST] - 새로운 비디오 생성
# [PUT] - X
# [DELETE] - X
class VideoList(APIView):
    def get(self):
        videos = Video.objects.all()
        # 직렬화 (Object → Json) : Serializer
        serializers = VideoSerializer(videos, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        serializer = VideoSerializer(data=user_data)

        if serializer.is_valid():
            video = serializer.save(user=request.data)   
            # serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. VideoDetail
# api/v1/video/{video_id}
# [GET] - 특정 비디오 조회
# [POST] - X
# [PUT] - 특정 비디오 업데이트
# [DELETE] - 특정 비디오 삭제
class VideoDetail():
    def get():
        pass

    def put():
        pass

    def delete():
        pass
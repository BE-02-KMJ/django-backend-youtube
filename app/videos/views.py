from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import VideoListSerializer, VideoDetailSerializer
from .models import Video

# Create your views here.
# Video와 관련된 REST API

# 1. VideoList
# api/v1/video
# [GET] - 전체 비디오 목록 조회
# [POST] - 새로운 비디오 생성
# [PUT] - X
# [DELETE] - X
class VideoList(APIView):
    def get(self, request):
        videos = Video.objects.all()
        # 직렬화 (Object → Json) : Serializer
        serializer = VideoListSerializer(videos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        serializer = VideoListSerializer(data=user_data)

        if serializer.is_valid():
            serializer.save(user=request.user)   
            # serializer = VideoSerializer(video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. VideoDetail
# api/v1/video/{video_id}
# [GET] - 특정 비디오 조회
# [POST] - X
# [PUT] - 특정 비디오 업데이트
# [DELETE] - 특정 비디오 삭제
class VideoDetail(APIView):
    def get(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise NotFound
        
        serializer = VideoDetailSerializer(video)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        video_obj = Video.objects.get(pk=pk)    # DB에서 불러온 데이터
        user_data = request.data    # user가 보낸 데이터
        
        serializer = VideoDetailSerializer(video_obj, user_data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        video_obj = Video.objects.get(pk=pk)
        video_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
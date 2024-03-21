from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import SubListSerializer, SubDetailSerializer
from .models import Subscription

# Create your views here.
# SubscriptionList
# api/v1/sub
# [POST] : 구독하기.
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data
        serializer = SubListSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# SubscriptionDetail
# api/v1/sub/{user_id}
# [GET] : 특정 유저의 구독자들 조회
# [DELETE] : 구독 취소
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        try:
            subscription = Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            raise NotFound
        
        serializer = SubDetailSerializer(subscription)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        sub_obj = Subscription.objects.get(pk=pk)
        sub_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import SubSerializer
from .models import Subscription

# Create your views here.
# SubscriptionList
# api/v1/sub
# [POST] : 구독하기.
class SubscriptionList(APIView):
    # def get(self, request):
    #     subs = Subscription.objects.filter(subscriber=request.user)
    #     serializer = SubSerializer(subs, many=True)
    #     return Response(serializer.data)
    
    def post(self, request):
        user_data = request.data
        serializer = SubSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# SubscriptionDetail
# api/v1/sub/{user_id}
# [GET] : 특정 유저의 구독자들 조회
# [DELETE] : 구독 취소
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        subs = Subscription.objects.filter(subscribed_to=pk)                
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import serializers
from .models import Subscription
from users.serializers import UserSerializer

class SubListSerializer(serializers.ModelSerializer):
    # Video:User - Video(FK) → User
    class Meta:
        model = Subscription
        fields = '__all__'

    # 내가 나를 구독할 수 없다. → 확인 필요.
    def validate(self, data):   # data (type) - Dict.
        if data['subscriber'] == data['subscribed_to']:
            raise serializers.ValidationError("You can't subscribe to yourself.")
        return data
    
class SubDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'

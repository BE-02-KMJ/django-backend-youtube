from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.
class Subscription(CommonModel):
    # User:Subscription - User(Subscriber) → subscriber(FK)
    # User:Subscription - User(Subscribed_to) → subscribed_to(FK)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')    # 내가 구독한 사람
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers') # 나를 구독한 사람
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import ChatRoom

# Create your tests here.
class ChatAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email = 'test@email.com',
            password = 'test123123',
        )
        self.client.login(email = 'test@email', password = 'test123123')

        self.chat = ChatRoom.objects.create(
            title = 'test chat room',
            user = self.user,
        )

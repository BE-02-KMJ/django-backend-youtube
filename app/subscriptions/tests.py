from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import Subscription

# Create your tests here.
class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email = 'test_main', password = 'password123')
        self.user2 = User.objects.create_user(email = 'test_sub', password = 'password000')
        self.client.login(email = 'test_main', password = 'password123')

    # def test_sub_list_get(self):
    #     url = reverse('sub-list')
    #     res = self.client.get(url)
    
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(res.data), 1)

    def test_sub_list_post(self):
        url = reverse('sub-list')
        data = {
            'subscriber': self.user1.pk,
            'subscribed_to': self.user2.pk
        }

        res = self.client.post(url,data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_sub_detail_get(self):
        Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        url = reverse("sub-detail", kwargs={"pk": self.user2.pk})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_sub_detail_delete(self):
        sub = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)

        url = reverse('sub-detail', kwargs={'pk': sub.id})

        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Subscription.objects.count(), 0)
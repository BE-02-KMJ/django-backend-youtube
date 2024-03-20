from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from users.models import User
from .models import Video

# Create your tests here.
class VideoAPITestCase(APITestCase):
    # setup - test code가 실행되기 전 동작하는 함수
    # 필요 항목 (1) 유저 생성(ORM) 및 로그인 (2) 비디오 생성 
    def setUp(self):
        self.user = User.objects.create_user(
            email = 'mjk@gmail.com',
            password = 'password123'
        )
        
        self.client.login(email='mjk@gmail.com', password='password123')

        # self를 적으면 지역변수가 된다! 유레카!
        self.video = Video.objects.create(
            title = 'test video',
            link = 'https://www.test.com',
            user = self.user
        )
    
    # Video List 관련 API
    def test_video_list_get(self):
        # url = 'http://127.0.0.1:8000/api/v1/video'
        # 위 처럼 url을 직접 적어서 불러와도 되지만
        # 주소가 조금이라도 바뀌면 계속 수정해줘야되기 때문에
        # urls.py 파일을 만들어 url만 따로 관리해준다.
        url = reverse('video-list')
        res = self.client.get(url)  # 전체 비디오 조회 데이터 (응답값)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertTrue(len(res.data) > 0)

        # Video의 title column이 응답 데이터에 잘 들어가 있는지 확인.
        for video in res.data:
            self.assertIn('title', video)

    def test_video_list_post(self):
        url = reverse('video-list')
        data = {
            'title': 'test video2',
            'link': 'https://test.com',
            'category' : 'test category',
            'thumbnail' : 'http://test.com',
            'video_file' : SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user' : self.user.pk
        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video2')

    # Video Detail 관련 API
    def test_video_detail_get(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        # url_ex) api/v1/video/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_video_detail_put(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
        data = {
            'title': 'updated video',
            'link': 'https://test.com',
            'category' : 'test category',
            'thumbnail' : 'http://test.com',
            'video_file' : SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user' : self.user.pk
        }

        res = self.client.put(url, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'updated video')

    def test_video_detail_delete(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
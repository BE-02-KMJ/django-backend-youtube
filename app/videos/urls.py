from django.urls import path
# from . import views
from .views import VideoList, VideoDetail

# api/v1/video
urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
    #{pk}
    path('<int:pk>', VideoDetail.as_view(), name='video-detail'),
]
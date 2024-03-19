from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.
class Video(CommonModel):
    title = models.CharField(max_length=30, required=True)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    video_file = models.FileField(upload_to='storage/')
    # FileField나 ImageField를 사용하면 Django에 저장되고 무거워지기 때문에 보통 사용하는 것을 추천하지 않는다.
    # 보통 파일 S3 Bucket 저장 → URL 생성 → URL 이용
    # 여기에 저장해보는 것도 해볼 예정 (video_file)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
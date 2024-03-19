from django.db import models

# Create your models here.
class CommonModel(models.Model):
    # 생성된 시간 - 고정 값.
    created_at = models.DateTimeField(auto_now_add=True)
    # 업데이트된 시간 - 유동 값. 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # DB에 Table 추가 X
        abstract = True
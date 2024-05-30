from django.db import models
from accounts.models import User


# Create your models here.

class ImageUpload(models.Model):
    filename = models.CharField("파일 이름", max_length=100, null = False, blank = True)
    img = models.ImageField("이미지", upload_to = 'images/', null = True, blank = True)
    img_caption = models.TextField("이미지 캡션", null=True, blank = True)
    # null은 DB에 저장될 때 빈 공간을 허용하는 옵션



    # admin 모드일 때 제목으로 파일 구분할 수 있음
    def __str__(self):
        return str(self.filename)
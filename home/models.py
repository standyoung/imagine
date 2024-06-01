from django.db import models
from accounts.models import User

# Create your models here.

class ImageUpload(models.Model):
    filename = models.CharField("파일 이름", max_length=100, null = False, blank = True)
    img = models.ImageField("이미지", upload_to = 'images/', null = True, blank = True)
    img_caption = models.TextField("이미지 캡션", null=True, blank = True)
    # null은 DB에 저장될 때 빈 공간을 허용하는 옵션

    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, verbose_name="사용자")
    # 이미지 업로드와 유저의 관계가 foreignkey로 연결
    # on_delete : 사용자가 삭제되면 그 사용자가 올린 것도 모두 지워버릴 것


    # admin 모드일 때 제목으로 파일 구분할 수 있음
    def __str__(self):
        return str(self.filename)

    class Meta:
        db_table = 'imageUpload'
        verbose_name = '이미지 업로드'
        verbose_name_plural = '이미지 업로드'

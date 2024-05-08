from django.conf import settings
from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField("아이디", max_length=40, default='', unique=True) # unique default false
    pwd = models.CharField("비밀번호", max_length=300, null=False) # 암호화 대비 넉넉하게
    username = models.CharField("이름", max_length=40, null=False)
    birth = models.DateField("생일", null=False)
    gender = models.CharField("성별",max_length=20, null=False)
    email = models.EmailField("이메일",max_length=300, null=False)

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['username','pwd','email']

    def __str__(self):
        return self.uid



from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    username = models.CharField("아이디", max_length=40, default='', unique=True) # unique default false
    password = models.CharField("비밀번호", max_length=300, null=False) # 암호화 대비 넉넉하게
    nickname = models.CharField("이름", max_length=40, null=False)
    birth = models.DateField("생일", null=False)
    gender = models.CharField("성별",max_length=20, null=False)
    email = models.EmailField("이메일",max_length=300, null=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname','password','email']

    def __str__(self):
        return self.username



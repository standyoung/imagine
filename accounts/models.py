from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager):
    # username과 password 상속받음
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("Users Must Have an email address")
        
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(email, nickname, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

# AbstarctUser을 상속한 모델을 만드는 방법
class User(AbstractUser):
    username = models.CharField("아이디", max_length=40, default='', unique=True) # unique default false
    password = models.CharField("비밀번호", max_length=300, null=False) # 암호화 대비 넉넉하게
    nickname = models.CharField("이름", max_length=40, null=False)
    birth = models.DateField("생일", null=False)
    gender = models.CharField("성별",max_length=20, null=False)
    email = models.EmailField("이메일",max_length=300, null=False)
    first_name = None
    last_name = None
    date_joined = None

    USERNAME_FIELD = 'username'  # for using for login

    # REQUIRED_FIELDS 변수에 추가된 필드를 넣어줘야 추후에 supseruser 생성 시에 해당 데이터도 입력 받음
    # password는 이미 REQUIRED_FIELDS 변수
    REQUIRED_FIELDS = ['email','nickname','birth','gender']

    def __str__(self):
        return self.username



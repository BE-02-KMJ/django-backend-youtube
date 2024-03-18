from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# CreateSuperuser
# - email (option)
# - nickname (required)
# - password
# - is_business: personal, business
class User(AbstractBaseUser, PermissionsMixin):
    # CharField → VARCHAR(255)
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)    # default
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # 유저를 생성 및 관리 (유저를 구분해서 관리하기 위해 - 관리자 계정, 일반 계정)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'email: {self.email}, nickname: {self.nickname}'
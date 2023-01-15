from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # 기본 사용자는 이미 사용자 이름, 이메일, 비밀번호 같은 것을 기억하고 있으므로
    # 여기에 one-to-one으로 추가적인 정보를 추가해야하기 때문입니다.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username

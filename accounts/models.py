from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractUser
# from .managers import CustomUserManager

#헬퍼클래스
class UserManager(BaseUserManager):

    def create_user(self, email,name, nickname, phone, birthday, address1, address2, address3, profile, password1, password2):
        if not email:
            raise ValueError('Users must have an email address')

        if not name:
            raise ValueError('Users must have an name')
        
        if not nickname:
            raise ValueError('Users must have an nickname')
        
        if not phone:
            raise ValueError('Users must have an phone number')
        
        if not birthday:
            raise ValueError('Users must have an birthday')
        
        if not address1:
            raise ValueError('Users must have an address1')
        
        if not address2:
            raise ValueError('Users must have an address2')
        
        if not address3:
            raise ValueError('Users must have an address3')
        
        
        # email = self.normalize_email(email)
        # username = self.model.normalize_username(username)

        # user = self.model(email=self.normalize_email(email), **extra_fields)
        user = self.model(
            email=self.normalize_email(email), 
            name=name,
            nickname = nickname,
            phone = phone,
            birthday = birthday,
            address1 = address1,
            address2 = address2,
            address3 = address3, 
            profile = profile
            )
        user.set_password(password1)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(email=email, password=password,)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

#실제 모델이 상속받아 생성하는 클래스가 Abstract
class  User(AbstractUser, PermissionsMixin):
    username = None

    user_id = models.AutoField(primary_key=True) 
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    password1 = models.CharField(max_length=30,  null=False, blank=False,default='password1')
    password2 = models.CharField(max_length=30,  null=False, blank=False,default='password2')
    name = models.CharField(max_length=30,  null=False, blank=False,default='name')          #실명
    nickname = models.CharField(max_length=30, null = True, default='nickname')              #별명
    phone = models.CharField(max_length=100, null=False, blank=False,default='phone')        #핸드폰 번호
    birthday = models.CharField(max_length=30,  null=False, blank=False,default='birthday')  #생년월일
    address1 = models.CharField(max_length=255, null=False, blank=False, default='address1') #우편번호
    address2 = models.CharField(max_length=255, null=False, blank=False, default='address2') #주소지
    address3 = models.CharField(max_length=255, null=False, blank=False, default='address3') #상세주소
    usertype = models.CharField(max_length=255, null=False, blank=False, default='usertype')  #구매자/판매자
    profile = models.ImageField(upload_to="", null = True, blank=True, default='')    #프로필
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    #User모델 필수 field
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #헬퍼클래스 사용
    objects = UserManager()

    #사용자 username필드는 email로 설정
    USERNAME_FIELD = 'email' #이메일로 로그인

    #필수 작성 필드
    REQUIRED_FIELDS = [email, name, nickname, phone, birthday, address1, address2, address3]

    

    def __str__(self):
        return"<%d %s>" % (self.pk, self.email)
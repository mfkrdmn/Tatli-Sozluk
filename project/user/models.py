from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField
# from django.contrib.gis.db import models as gismodels


class UserManager(BaseUserManager):
    def create_user(self, nick, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not nick:
            raise ValueError('User must have an nick')

        user = self.model(
            email = self.normalize_email(email),
            nick = nick,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nick, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            nick = nick,
            password = password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    nick = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nick']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.user

    #here we are using django signals to create upserprofile automatically after having a user
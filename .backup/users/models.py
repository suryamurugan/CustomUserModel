from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime  


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, usn, password=None,):
        user = self.model(
            email=self.normalize_email(email),
            usn=usn,
            name=name,
            is_staff=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, usn, password):
        user = self.create_user(
            email,
            password=password,
            usn=usn,         
            name=name,
            is_staff=True,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, usn, password):
        user = self.create_user(
            email,
            password=password,
            usn=usn,
            name= "True",
            is_staff=True,
        )
        #user.admin = True
        user.save(using=self._db)
        return user


class aitUser(AbstractBaseUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    is_staff = models.BooleanField(('staff status'),default=False)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'usn','name' ]
    def __str__(self):              # __unicode__ on Python 2
        return self.email

    objects = UserManager()

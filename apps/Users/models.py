from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, is_staff = False, is_superuser=False, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)
    
        
class User(models.Model):
    email = models.EmailField('Correo Electronico', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'users'


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from relationship_app.models import Book


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        
        #Validating Email
        if not email:
            raise ValueError('User must have an email address')
        #Fetching and normalizing email
        user = self.model(email=self.normalize_email(email), **extra_fields)

        #Setting password (hashes password)
        user.set_password(password)
        #saving created user in current database
        user.save(using=self._db)
        #returning created user
        return user
    
    #creating superuser ensuring administrative users can be created with the required fields fields
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
#Custom User Model by extending AbstractUser
#from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default='2020-01-01', blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    objects = CustomUserManager()
    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField(default = '2020-01-01')
    modified_by = models.ForeignKey()

#Extending Book Model with Custom Permissions
    class Meta:
        permissions =(
            ('can_create', 'Can create'),
            ('can_view', 'Can view'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),

        )

    def __str__(self):
        return f"{self.title} by {self.author} published on {self.publication_date}"



    class Meta:
        permissions = [
            ('can_view', 'Can view'),
            ('can_create', 'Can create'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),
        ]       
          
   
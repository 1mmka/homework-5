from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(max_length=32)
    avatar = models.ImageField(upload_to='uploads\profile-pictures')
    
    def __str__(self):
        return self.username

class UserComments(models.Model):
    content = models.CharField(max_length=64)
    file = models.ImageField(upload_to='uploads\post-pictures',validators=[validators.FileExtensionValidator(
        allowed_extensions=('gif','jpeg','png','ico','tiff','webp','eps','svg','psd','indd','cdr','ai','raw')
    )])
    user_creator = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='creator')
    
    def __str__(self):
        return self.content[0:11:1]
from django.db import models
from common.models import BaseModel
from django.contrib.auth import get_user_model
import uuid
# Create your models here.
User = get_user_model()

class Profile(BaseModel):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_img = models.ImageField(upload_to='users/profile_img/', default='blank-profile-img.png')


    def __str__(self):
        return f"{self.name}_{self.id}_profile"
    


from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING 

# Create your models here.

class user_profile(models.Model):
    address = models.TextField()
    dob = models.DateField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User,on_delete=CASCADE)
from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    # ONE user should have ONE userprofile and ONE userprofile should have ONE user.
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    # One user should have one userprofile and one userprofile should have one user.
    user = models.OneToOneField(User, related_name='userprofile',
                                # Userprofile is deleted when User gets deleted
                                on_delete=models.CASCADE)

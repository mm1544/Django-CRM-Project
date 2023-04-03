# User needed to know who has created a Team
from django.contrib.auth.models import User
from django.db import models

# Subscription Plan
class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    max_leads = models.IntegerField()
    max_clients = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    # ConnectingPlan and Team models
    plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # To reference all the members of a Team. Will use here many2many field.
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE) # When deleting User, Team will also be deleted
    created_at = models.DateTimeField(auto_now_add=True)

    # To display Tem name on Admin dashboard
    def __str__(self):
        return self.name



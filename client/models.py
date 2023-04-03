from django.contrib.auth.models import User
from django.db import models

from team.models import Team

class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE) # 'CASCADE' --> When deleting User all the related leads will be DELETED.
    created_at = models.DateTimeField(auto_now_add=True) # 'auto_now_add' --> Field will be filled automatically.
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Will order Clients alphabetically
        ordering = ('name',)

    # Will show a Lead name on Admin dashboard
    def __str__(self):
        return self.name
        # return '{} - {}'.format(self.name, self.modified_at)
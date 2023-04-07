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


class ClientFile(models.Model):
    team = models.ForeignKey(Team, related_name='client_files', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='clientfiles')
    created_by = models.ForeignKey(User, related_name='client_files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Will show a Client name on Admin dashboard
    def __str__(self):
        return self.created_by.username


class Comment(models.Model):
    team = models.ForeignKey(Team, related_name='client_comments', on_delete=models.CASCADE)
    # When Client is deleted, then the Comment is deleted as well(?) --> 'on_delete=models.CASCADE'
    client = models.ForeignKey(Client, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='client_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Will show a Lead name on Admin dashboard
    def __str__(self):
        return self.created_by.username
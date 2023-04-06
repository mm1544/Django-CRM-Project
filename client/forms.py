from django import forms

from .models import Client, Comment

# We use 'ModelForm' because Django will automatically create form for us based on information we will set in this class.
class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'description')


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

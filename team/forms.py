from django import forms

from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name',)

# Now we can import this form into Views
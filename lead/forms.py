from django import forms

from .models import Lead

# We use 'ModelForm' because Django will automatically create form for us based on information we will set in this class.
class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status')

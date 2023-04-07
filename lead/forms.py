from django import forms

from .models import Lead, Comment, LeadFile

# We use 'ModelForm' because Django will automatically create form for us based on information we will set in this class.
class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status')

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ('file',)
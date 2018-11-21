from django import forms
from .models import Site,Profile

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        exclude = ['profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Site
        exclude = ['link','description','profile','image','title']

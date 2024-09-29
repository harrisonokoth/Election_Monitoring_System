from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['election', 'title', 'description', 'location', 'evidence']

    widgets = {
        'description': forms.Textarea(attrs={'rows': 5}),
        'location': forms.TextInput(attrs={'placeholder': 'Enter the location'}),
    }

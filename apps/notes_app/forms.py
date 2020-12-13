from django import forms
from django.core.exceptions import ValidationError
from .models import Note, Description

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Insert note title here...'})
        }

class DescForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description here...'}), label='')
    class Meta:
        model = Description
        fields = ['content']

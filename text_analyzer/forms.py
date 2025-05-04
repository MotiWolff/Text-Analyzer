from django import forms
from .models import TextAnalysis
from django.utils.safestring import mark_safe

class TextAnalysisForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 10,
            'placeholder': 'Paste your text here...',
            'style': 'resize: vertical;'
        }),
        required=True,
        label=mark_safe('<i class="fas fa-file-alt me-1"></i> Text Content')
    )
    
    class Meta:
        model = TextAnalysis
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional title for your analysis'
            })
        }

class FileUploadForm(forms.Form):
    file = forms.FileField(
        label=mark_safe('<i class="fas fa-upload me-1"></i> Upload File'),
        help_text='Supported formats: .txt, .doc, .docx, .pdf',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.txt,.doc,.docx,.pdf'
        })
    )
    title = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Optional title for your analysis'
        })
    )
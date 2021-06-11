from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'student_name': forms.TextInput(attrs={'class': "form-control mb-3 mt-2", 'placeholder':"Your name"}),
            'project_name': forms.TextInput(attrs={'class': "form-control mb-3 mt-2", "placeholder":"Name of your project"}),
            "subtitle": forms.TextInput(attrs={'class': "form-control mb-3 mt-2", "placeholder":"A short description of your project"}),
            "description": forms.Textarea(attrs={'class': "form-control mb-3 mt-2", "placeholder":"Project details, technologies and tools used, etc", "rows": "5"}),
            "links": forms.Textarea(attrs={'class': "form-control mb-3 mt-2", "placeholder":"links to the project, source code, etc", "rows": "3"}),
            "contact": forms.Textarea(attrs={'class': "form-control mb-3 mt-2", "placeholder":"Email address, facebook ID, etc", "rows": "3"}),
        }
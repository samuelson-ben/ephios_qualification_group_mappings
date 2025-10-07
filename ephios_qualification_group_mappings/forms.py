from django import forms

from ephios_qualification_group_mappings.models import QualificationGroupMapping

class QualificationGroupMappingForm(forms.ModelForm):
    class Meta:
        model = QualificationGroupMapping
        fields = ['qualification', 'group']
        widgets = {
            'qualification': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }